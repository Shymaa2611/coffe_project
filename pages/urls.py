from django.urls import path
from . import views
urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog.as_view(),name='blog'),
    path('coffes',views.coffes.as_view(),name='coffes'),
    path('contact',views.contact.as_view(),name='contact'),
    path('new_coffe',views.add_new_Coffe.as_view(),name='new_coffe'),
    path('shop',views.shop.as_view(),name='shop')
]
