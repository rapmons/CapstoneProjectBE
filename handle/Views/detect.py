
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.words import wordsSerializer
from ..models import words
from fastai.vision.all import *
from fastai.vision.widgets import *
class createHistoryWordsView(APIView):
    def post(self, request):
        new_model = load_learner('E:/Desktop/gitclone/FastAI-Image-Classification/dataset/fruit_classifier.pkl')
        image = request.FILES.get('url')
        img = Image.open(image)
        img = img.resize((224, 224))
        img = img.convert('RGB')
        result,_,pos=new_model.predict(img
)       
        word= words.objects.filter(text=str(result.capitalize())).first()
        hehe= wordsSerializer(word)
        return Response({"result":hehe.data,"post":pos.max()})
       
        
        
