
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.words import wordsSerializer
from ..models import words,myWords,users
from .Caption1 import caption_this_image
from PIL import Image
import keras
from io import BytesIO
class createHistoryWordsView(APIView):
     def post(self, request):
        image = request.FILES.get('url')
      
        image_data = BytesIO(image.read())
        img = keras.utils.load_img(image_data,target_size=(224,224))
        caption = caption_this_image(img)
        result_dic = {
                     "caption" : caption
                     }
        return Response(result_dic)
        
    
   
        
        

        
       
        
        
