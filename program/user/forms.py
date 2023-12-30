from django.contrib.auth import forms as auth_forms
from django import forms

from . import models

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = (
            'email', 'first_name', 'last_name', "password1", "password2", 'get_update'
        )

class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = models.User
        fields = (
            'units', 'first_name', 'last_name', 'email', 'get_update'
        )
        exclude = ('password', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')

class CreaterForm(forms.ModelForm):
    class Meta:
        model = models.Creater
        fields = ('photo', 'about', )
