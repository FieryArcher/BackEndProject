from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    favorites = models.ManyToManyField("self", blank=True)
    phone = models.CharField(max_length=50)
    is_author = models.BooleanField(default=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
