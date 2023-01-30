from rest_framework import generics
from .models import CNABFile
from .serializers import CNABUploadForm

class CNABView(generics.CreateAPIView):
    serializer_class = CNABUploadForm
    queryset = CNABFile.objects.all()
