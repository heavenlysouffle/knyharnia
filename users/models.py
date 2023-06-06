from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import uuid
import requests


def validate_real_email(email_address):
    team_slug = 'ponchikdoch'
    api_key = 'Zq1nLAIP.Qgk3B2BdxZRiF7ohr3rZ7m26jsr4W6PO'

    response = requests.post(
        "https://app.mailvalidation.io/a/" + team_slug + "/validate/api/validate/",
        json={'email': email_address},
        headers={
            'content-type': 'application/json',
            'accept': 'application/json',
            'Authorization': 'Api-Key ' + api_key,
        },
    )
    valid = response.json()['is_valid']
    if not valid:
        raise ValidationError(
            _("%(email_address) is not real email address"),
            params={'email_address': email_address},
        )


class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=20, unique=True, validators=[
        RegexValidator(
            regex='^\w{4,20}$',
            message='Username doesn\'t comply',
        ),
    ])
    password = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='[\w@$!%*?&]{4,20}',
            message='Password doesn\'t comply'
        ),
    ])
    email = models.CharField(max_length=50, unique=True, validators=[validate_real_email])
    email_notifications = models.BooleanField(default=True)


class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    follows_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows_who')

    # TODO: validate record uniqueness
