from django.db import models
from users.models import User
from fandoms.models import Fandom
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Relationship(models.Model):
    character1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character1')
    character2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character2')

    # TODO: validate record uniqueness


class Fanfic(models.Model):
    class Rating(models.Model):
        # TODO filling: General Audiences, Teen And Up Audiences, Mature, Explicit
        title = models.CharField(max_length=21, unique=True)

    class Categories(models.Model):
        # TODO filling: F/F, F/M, Gen, M/M, Multi, Other
        title = models.CharField(max_length=5, unique=True)

    class Tags(models.Model):
        title = models.CharField(max_length=60, unique=True, editable=False)

    title = models.CharField(max_length=40)
    summary = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fandoms = models.ManyToManyField(Fandom, blank=True)
    published_date = models.DateField()
    last_update_date = models.DateField()
    rating = models.ForeignKey(Rating, blank=True, null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tags, blank=True)
    characters = models.ManyToManyField(Character, blank=True)
    relashionships = models.ManyToManyField(Relationship, blank=True)

    # Likes
    # Chapters
    # Bookmarks

    def validate_published_date(self):  # TODO: at what moment are date validators used
        if self.published_date != datetime.today().strftime('%Y-%m-%d'):
            raise ValidationError(
                _("%(published_date) hasn't come yet"),
                params={'published_date': self.published_date},
            )

    def validate_last_update_date(self):
        if self.last_update_date != datetime.today().strftime('%Y-%m-%d'):  # TODO: decorator
            raise ValidationError(
                _("%(last_update_date) hasn't come yet"),
                params={'last_update_date': self.last_update_date},
            )
        if self.last_update_date > self.published_date:
            raise ValidationError(
                _("%(last_update_date) cannot be more than published_date"),
                params={'last_update_date': self.last_update_date},
            )
