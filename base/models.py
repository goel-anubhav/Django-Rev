from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)