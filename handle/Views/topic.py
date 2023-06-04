import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.users import usersSerializer
from ..models import users,myWords,words,historyResult,topic
from ..Serializer.myWords import myWordsSerializer
from ..Serializer.topic import topicSerializer
from ..Serializer.words import wordsSerializer
from django.db.models.functions import Random
from django.http import JsonResponse

import jwt
class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

class Game(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        list_word=list(words.objects.all())
        quiz_questions =words.objects.filter(topic_id=request.data["idTopic"]).order_by(Random())
            
        questions = []
        for quiz_question in quiz_questions:
            qu=[]
            textRandom= list( random.sample(list_word,3))
            qu.append(textRandom[0].mean)
            qu.append(textRandom[1].mean)
            qu.append(textRandom[2].mean)
            qu.append(quiz_question.mean)
            hehe=list(random.sample(qu,4))
            
            
            question = {
                'question': quiz_question.url,
                'text':quiz_question.text,
                'answers': hehe,
                'correctAnswerIndex':hehe.index(quiz_question.mean),
            }
            questions.append(question)
        return JsonResponse(questions, safe=False)

class getListWord(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        listWord= words.objects.filter(topic_id=request.data["idTopic"])
        serializer =wordsSerializer(listWord, many=True)
        return Response(serializer.data)
class getResultWord(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        listTopic= topic.objects.filter()[1:]
        result=[]
        for to in listTopic:
            he= historyResult.objects.filter(users=user,topic=to).first()
            listw=words.objects.filter(topic=to).count()
            serializer = topicSerializer(to)
            if he ==None:
                re={
                    "topic":serializer.data,
                    "number":listw,
                    "pos":0

                }
            else:
                 re={
                    "topic":serializer.data,
                    "number":listw,
                    "pos":he.numberQT

                }
            result.append(re)



        return JsonResponse(result, safe=False)

	

