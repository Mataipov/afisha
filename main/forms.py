from django import forms
from django.core.exceptions import ValidationError
from .models import Film, Director
from django.contrib.auth.models import User


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "title", "author", "rating", "duration"
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title).count() > 0:
            raise ValidationError("Film already exists!!!")
        return title


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']
        widgets = {
            'director': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name):
            raise ValidationError('Director with this name already exists')
        return name

class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError('User already exists with this username')
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError('Passwords does not match')
        return password1


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))