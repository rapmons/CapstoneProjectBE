
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.historySearch import historySearchSerializer
from ..models import users,historySearch
import jwt
class historyView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        history= historySearch.objects.filter(users_id=user.id, delete=0).order_by('-id')
        his=[]
        for i in history:
            his.append(i.idSearch)
        return Response(his)
class createView(APIView):
     def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = users.objects.filter(username=payload['username']).first()
        word1= historySearch.objects.filter(idSearch=request.data['idWord'],users=user).first()
        
        if word1 !=None:
           historySearch.objects.filter(idSearch=request.data['idWord'],users=user).update(
              delete=request.data['saved']
            
            )
        else:
             historySearch.objects.create(
               users=user,
               delete=request.data['saved'],
               idSearch=request.data['idWord']
                
            )
        if request.data["saved"]:
             return Response("Delete successfuly !")
        else :
             return Response("Save successfuly !")
       
