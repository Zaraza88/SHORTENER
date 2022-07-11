from django.db import models
from django.contrib.auth.models import User


class URLModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_url = models.URLField("оригинальный url")
    modified_url = models.URLField("измененный url")
