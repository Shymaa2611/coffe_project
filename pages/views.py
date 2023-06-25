from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import userForm

def index(request):
    return render(request,"pages/index.html")
def about(request):
    return render(request,"pages/about.html")
def blog(request):
    return render(request,"pages/blog.html")
def contact(request):
    if request.method=='POST':
        data_save=userForm(request.POST,request.FILES)
        if data_save.is_valid():
            data_save.save()
            return redirect('/')
    context={
        'form':userForm()
    }
    return render(request,"pages/contact.html",context)
def coffes(request):
    return render(request,"pages/coffes.html")
def shop(request):
    return render(request,"pages/shop.html")