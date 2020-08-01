from django import forms
from .models import entry
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class student(forms.ModelForm):
    class Meta:
        model = entry
        fields = ['name', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'})
        }
class singup(UserCreationForm):
    password1=forms.CharField(label=" Password",widget=forms.PasswordInput(attrs={'class':'form-control'}) ,required=True)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}) ,required=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        labels = {'email': 'email'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }