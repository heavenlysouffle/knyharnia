from django.db import models


class Fandom(models.Model):
    title = models.CharField(max_length=100, unique=True)
