from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['game_name', 'plataform', 'genre', 'release_year', 'review', 'score', 'cover']
        error_messages = {
                    'game_name': {'required': ('Debe agregar el nombre del juego'),},
                    'plataform': {'required': ('Debe agregar la plataforma'),},
                    'genre': {'required': ('Debe agregar el género del juego'),},
                    'release_year': {'required': ('Debe agregar el año de lanzamiento'),},
                    'review': {'required': ('Debe escribir una review'),},
                    'score': {'required': ('Debe otorgar una valoración'),},
            }
            
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Username',
            'email': 'Email',
        }
        
