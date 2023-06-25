from django.shortcuts import render
from django.views.generic import ListView

def index(request):
    return render(request,"pages/index.html")
def about(request):
    return render(request,"pages/about.html")
def blog(request):
    return render(request,"pages/blog.html")
def contact(request):
    return render(request,"pages/contact.html")
def coffes(request):
    return render(request,"pages/coffes.html")