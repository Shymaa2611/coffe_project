from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from .forms import userForm,coffeForm
from .models import userData,Coffee,Blog

class index(CreateView):
    model=userData
    form_class=userForm
    template_name="pages/index.html"
    success_url='/'
    context_object_name='form'


def about(request):
    return render(request,"pages/about.html")

class blog(ListView):
    model=Blog
    template_name="pages/blog.html"
    context_object_name='blo'
class contact(CreateView):
    model=userData
    form_class=userForm
    template_name="pages/contact.html"
    success_url='/'
    context_object_name='form'

class coffes(ListView):
    model=Coffee
    template_name='pages/coffes.html'
    context_object_name='cof'
class add_new_Coffe(CreateView):
    model=Coffee
    form_class=coffeForm
    template_name='pages/add_new_coffe_type.html'
    context_object_name='form'

class shop(ListView):
    model=userData
    template_name="pages/shop.html"
    success_url='/'
    context_object_name='clients'
