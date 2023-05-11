import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.users import usersSerializer
from ..models import users,myWords,words
from ..Serializer.myWords import myWordsSerializer

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
        list_word= list(words.objects.all())
        myWord= list(myWords.objects.filter(users_id=user.id).order_by('-id')[:10])
        result_list = ["A", "B", "C", "D"]
        questtion=list()
        for i in myWord:
            mapArray= my_dictionary()
            textRandom= list( random.sample(list_word,3))
            result= list( random.sample(result_list,4))
            mapArray.add(result[0],i.word.text)
            mapArray.add(result[1],textRandom[0])
            mapArray.add(result[2],textRandom[1])
            mapArray.add(result[3],textRandom[2])
            mapArray.add("true", result[0])
            mapArray.add("question",i.url)
            questtion.append(mapArray)
            
        return Response(questtion)

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
        serializer = myWordsSerializer(myWord, many=True)
        return Response(serializer.data)
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
        word1= words.objects.filter(id=request.data['id_word']).first()
        myWords.objects.create(
             word=word1,
             users=user,
             saveF=True,
             url=request.data['url']
        )
        return Response("Save successfuly !")

class WordSavedView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        myWord= myWords.objects.filter(users_id= user.id, saveF= 0).order_by('-id')
        serializer = myWordsSerializer(myWord, many=True)
        return Response(serializer.data)
	

