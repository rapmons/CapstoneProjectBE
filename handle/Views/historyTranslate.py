
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.historyTranslate import historyTranslateSerializer
from ..models import users,historyTranslate
import jwt
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
        history= historyTranslate.objects.filter(users_id=user.id).order_by('-id')
        serializer = historyTranslateSerializer(history, many=True)
        return Response(serializer.data)
class createHistoryWordsView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        his= historyTranslate()
        his.users=user
        his.text= request["text"]
        his.mean= request["mean"]
        serializer =historyTranslateSerializer(data=his)
        if serializer.is_valid():
            serializer.save()
        
        return Response("Create successfuly !")
