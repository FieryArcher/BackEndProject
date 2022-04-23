from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AddPostForm(forms.Form):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="My Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
