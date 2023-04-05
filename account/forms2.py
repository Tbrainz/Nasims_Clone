from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RegisterProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'