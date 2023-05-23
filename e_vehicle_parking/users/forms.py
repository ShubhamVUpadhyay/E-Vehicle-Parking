from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
class Register(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': "text", 'class': "form-control", 'name': "username", 'placeholder': "Username", 'required': 'required','autocomplete':'off'})
        self.fields['email'].widget.attrs.update({'type': "email", 'class': "form-control", 'name': "email", 'placeholder': "Email", 'required': 'required','autocomplete':'off'})
        self.fields['first_name'].widget.attrs.update({'type': "text", 'class': "form-control  ", 'name': "first_name", 'placeholder': "First Name", 'required': 'required','autocomplete':'off'})
        self.fields['last_name'].widget.attrs.update({'type': "text", 'class': "form-control ", 'name': "last_name", 'placeholder': "Last Name",'required': 'required','autocomplete':'off'})
        self.fields['password1'].widget.attrs.update({'type': "password", 'class': "form-control ", 'name': "password1", 'placeholder': "Password",'required': 'required','autocomplete':'off'})
        self.fields['password2'].widget.attrs.update( {'type': "password", 'class': "form-control ", 'name': "password2", 'placeholder': "Confirm Password",'required': 'required','autocomplete':'off'})


    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class changePass(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'type': "password", 'class': "form-control", 'name': "old_password", 'placeholder': "Old Password", 'required': 'required','autocomplete':'off'})
        self.fields['new_password1'].widget.attrs.update({'type': "password", 'class': "form-control", 'name': "new_password1", 'placeholder': "New Password", 'required': 'required','autocomplete':'off'})
        self.fields['new_password2'].widget.attrs.update({'type': "password", 'class': "form-control  ", 'name': "new_password2", 'placeholder': "Confirm Password", 'required': 'required','autocomplete':'off'})




