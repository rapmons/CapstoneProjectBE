from rest_framework import serializers
from handle.models import words

class wordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = words
		fields ='__all__'