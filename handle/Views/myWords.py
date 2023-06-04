import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.users import usersSerializer
from ..models import users,myWords,words
from ..Serializer.myWords import myWordsSerializer
from django.db.models.functions import Random
from django.http import JsonResponse

import jwt
class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

class GameView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        list_word=list(words.objects.all())
        quiz_questions = myWords.objects.filter(users=user,saveF=True).order_by(Random())[:10]
            
        questions = []
        for quiz_question in quiz_questions:
            qu=[]
            textRandom= list( random.sample(list_word,3))
            qu.append(textRandom[0].text)
            qu.append(textRandom[1].text)
            qu.append(textRandom[2].text)
            qu.append(quiz_question.word.text)
            hehe=list(random.sample(qu,4))
            
            
            question = {
                'question': quiz_question.url,
                'text':quiz_question.word.mean,
                'answers': hehe,
                'correctAnswerIndex':hehe.index(quiz_question.word.text),
            }
            questions.append(question)
        return JsonResponse(questions, safe=False)

class historyWordsView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
       
        myWord= myWords.objects.filter(users_id=user.id).order_by('-id')
        resul=[]
        for i in myWord:
            qu={
                "id":i.id,
                "text":i.word.text,
                "mean":i.word.mean,
                "spell":i.word.spell,
                "type":i.word.wordType,
                "url":i.url,
                "saved":i.saveF
            }
            resul.append(qu)
        return JsonResponse(resul, safe=False)   

class saveWordsView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        word1= words.objects.filter(id=request.data['idWord']).first()
        savedWord= myWords.objects.filter(word=word1,users=user).first()
        if savedWord !=None:
           myWords.objects.filter(word=word1,users=user).update(
                saveF=request.data['saved'], 
            )
        else:
             myWords.objects.create(
                word=word1,
                users=user,
                saveF=request.data['saved'],
                url=request.data['url']
            )
        if request.data['saved']:
            return Response("Save successfuly !")

        return Response("Delete successfuly !")

class WordSavedView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        myWord= myWords.objects.filter(users=user,saveF=True).order_by('id')
        resul=[]
        for i in myWord:
            qu={
                "id":i.id,
                "text":i.word.text,
                "mean":i.word.mean,
                "spell":i.word.spell,
                "type":i.word.wordType,
                "url":i.url,
                "saved":i.saveF
            }
            resul.append(qu)
        return JsonResponse(resul, safe=False)   
	

