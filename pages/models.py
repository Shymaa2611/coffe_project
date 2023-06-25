from django.db import models

class userData(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    user_phone=models.CharField(max_length=100)
    message=models.TextField()

