# Third party imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Local application import
from .models import Post

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['document']
