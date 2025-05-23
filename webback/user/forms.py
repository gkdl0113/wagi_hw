# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment  # ✅ 이 줄이 반드시 있어야 함

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
