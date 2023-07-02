from rest_framework import serializers
from handle.models import historyResult

class historyResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = historyResult
		fields ='__all__'