
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import Emailwithattachment

from django.forms.widgets import PasswordInput, TextInput


# - Create/Register a user (Model Form)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class EmailwithattachmentForm(forms.ModelForm):
      
      sender_email_password = forms.CharField(widget=PasswordInput())
      
      class Meta:
            model = Emailwithattachment
            fields = ['sender_email_address', 'sender_email_password', 'receiver_name', 'receiver_email_address', 'stegano_image']