
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..Serializer.historyTranslate import historyTranslateSerializer
from ..models import words,topic

import json
class Command(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('file')
        vocabulary_list = json.load(file)
        hehe= topic.objects.create(
            id=1,
            name='detect'
        )
        for vocabulary in vocabulary_list:
            words.objects.create(
                text=vocabulary['text'],
                mean=vocabulary['mean'],
                spell=vocabulary['spell'],
                wordType=vocabulary['word_type'],
                topic=hehe,
                url=vocabulary['url_topic']
            )

        return Response({'message': 'Vocabulary imported successfully.'})

    
       
        
        
