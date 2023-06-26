from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class signUp(CreateView):
    form_class=UserCreationForm
    template_name="authentication/signUp.html"
    context_object_name="form"
    

