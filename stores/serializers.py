from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    store_name = serializers.CharField()
    owner = serializers.CharField()
        
    def create(self, validated_data):
        store = Store.objects.get_or_create(**validated_data)
        return store[0]

