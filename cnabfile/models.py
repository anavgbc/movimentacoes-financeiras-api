from django.db import models

class CNABFile(models.Model):
    file = models.FileField(upload_to='cnab_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
