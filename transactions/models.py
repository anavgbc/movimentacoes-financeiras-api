from django.db import models

class Transaction(models.Model):
    type = models.PositiveIntegerField()
    date = models.DateField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.DateTimeField()
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name="transactions")