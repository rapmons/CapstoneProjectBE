from rest_framework import serializers
from handle.models import historySearch
class historySearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = historySearch
		fields ='__all__'