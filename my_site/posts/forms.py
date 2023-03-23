from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'forms'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'forms'
    }))
    class Meta:
        model = Users
        fields = ('username','password')

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'forms'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'forms'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'forms'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'forms'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'forms'
    }))
    class Meta:
        model = Users
        fields = ('username','phone','email','password1','password2')

class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'name': forms.HiddenInput(),
                   'post': forms.HiddenInput()}