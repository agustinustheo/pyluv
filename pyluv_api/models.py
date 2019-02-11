from django.db import models
from pyluv_home.models import User

# Create your models here.

class API(models.Model):
    title = models.CharField(max_length=140)
    documentation = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    base_url = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title

class APIUrl(models.Model):
    api_name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=200)
    base_api = models.ForeignKey(API, on_delete=models.CASCADE)

    def __str__(self):
        return self.url