from rest_framework import serializers
from handle.models import myWords

class myWordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = myWords
		fields ='__all__'