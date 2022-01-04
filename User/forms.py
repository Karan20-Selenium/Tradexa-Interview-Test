from django.core import validators
from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _


class PostRegistration(forms.ModelForm):

    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()

    class Meta:
        model = Post
        fields = ['user','text','created_at','updated_at']
        labels = {'user':'User','text':'Text','created_at':'Created_At','updated_at':'Updated_At'}  
        widgets = {
            'text': forms.TextInput(attrs={'class':'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control'}),

            }

class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs=
    {'autofocus':True, 'class':'form-control'}))

    password = forms.CharField(label=_("Password"),strip=False, 
    widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password', 'class':'form-control'}))

