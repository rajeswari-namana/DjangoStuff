from django import forms
from emailApp.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
