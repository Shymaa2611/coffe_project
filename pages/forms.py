from django import forms
from .models import userData,Coffee


class userForm(forms.ModelForm):
    class Meta:
        model=userData
        fields='__all__'
class coffeForm(forms.ModelForm):
    class Meta:
        model=Coffee
        fields='__all__'