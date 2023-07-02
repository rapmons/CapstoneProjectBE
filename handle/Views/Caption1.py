

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
import pickle
from keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model, load_model
from keras_preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Input, Dense, Dropout, Embedding, LSTM
from keras.layers import Concatenate
from django.apps import AppConfig
import os

model_directory = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(model_directory, 'modelWeights', 'model6.h5')

word_to_index_path = os.path.join(model_directory, 'modelWeights', 'word_to_index.pkl')
index_to_word_path = os.path.join(model_directory, 'modelWeights', 'index_to_word.pkl')
   
model = load_model(model_file_path)
model.make_predict_function()
model_temp = ResNet50(weights="imagenet",input_shape=(224,224,3))

model_resnet = Model(model_temp.input,model_temp.layers[-2].output)
model_resnet.make_predict_function()


def preprocess_img(img):
    img = keras.utils.img_to_array(img)
    img = np.expand_dims(img,axis=0)
    # Normalisation
    img = preprocess_input(img)
    return img

def encode_image(img):
    img = preprocess_img(img)
    feature_vector = model_resnet.predict(img)
    
    feature_vector = feature_vector.reshape((1,feature_vector.shape[1]))
    #print(feature_vector.shape)
    return feature_vector


def predict_caption(photo):
    
    in_text = "startseq"
    max_len = 35
    for i in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence],maxlen=max_len,padding='post')
        
        ypred = model.predict([photo,sequence])
        ypred = ypred.argmax() #Word with max prob always - Greedy Sampling
        #print(ypred)
        word = idx_to_word[ypred]
        in_text += (' ' + word)
        
        if word == "endseq":
            break
    
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption





with open(word_to_index_path,"rb") as w2i:
    word_to_idx = pickle.load(w2i)

with open(index_to_word_path ,"rb") as i2w:
    idx_to_word = pickle.load(i2w)   
    


idx_to_word[1846] = "startseq"
word_to_idx["startseq"] = 1846

idx_to_word[1847] = "endseq"
word_to_idx["startseq"] = 1847


def caption_this_image(image):
    enc_img = encode_image(image)
    
    caption = predict_caption(enc_img)
    
    return caption


