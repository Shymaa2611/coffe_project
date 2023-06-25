from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('coffes',views.coffes,name='coffes'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop')
]
