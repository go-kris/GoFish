from django.db import models

# Create your models here.


class UpdateRequest(models.Model):
    email = models.EmailField()