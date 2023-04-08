from rest_framework import serializers
from handle.models import historyTranslate

class historyTranslateSerializer(serializers.ModelSerializer):
	class Meta:
		model = historyTranslate
		fields ='__all__'