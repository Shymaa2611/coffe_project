from django import forms
from .models import userData
class userForm(forms.ModelForm):
    class Meta:
      model=userData
      fields='__all__'