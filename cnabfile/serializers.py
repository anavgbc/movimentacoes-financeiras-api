from rest_framework import serializers
from .models import CNABFile
from utils.convert import convert_file
from stores.serializers import StoreSerializer
from transactions.serializers import TransactionSerializer

class CNABUploadForm(serializers.ModelSerializer):
    class Meta:
        model = CNABFile
        fields = "__all__"

    def create(self, validated_data):
        # print(validated_data)
        file = CNABFile.objects.create(**validated_data)
        # print(convert_file())
        converted = convert_file()

        for data in converted:
            store_name = data.pop("store_name")
            owner = data.pop("owner")
            store_dict = dict(store_name = store_name, owner = owner)
            
            serializer_store = StoreSerializer(data=store_dict)
            serializer_store.is_valid(raise_exception=True)
            store = serializer_store.save()
            data["store"] = store.id

            serializer_transactions = TransactionSerializer(data=data)
            serializer_transactions.is_valid(raise_exception=True)
            serializer_transactions.save()

        return file 




