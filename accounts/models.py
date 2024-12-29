from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    gender = models.CharField(
        max_length=1,
        choices=[('M', '남성'), ('F', '여성')],
        null=True,
        blank=True
    )
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField(
        'self',
        related_name='following',
        symmetrical=False,
        blank=True
    ) 