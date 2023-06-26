from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns=[
    path('',views.signUp.as_view(),name='signUp'),
    path('login',auth_view.LoginView.as_view(template_name='authentication/login.html'),name='login'),
    path('logout',auth_view.LogoutView.as_view(),name='logout'),
]
