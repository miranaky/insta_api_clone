from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_NOT_TO_SAY = "not to say"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
        (GENDER_NOT_TO_SAY, "Not to say"),
    )

    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    website = models.CharField(max_length=80, blank=True)
    phone_number = models.CharField(max_length=17, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20, blank=True)
    verified_badge = models.BooleanField(default=False)
