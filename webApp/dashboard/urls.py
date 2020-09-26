from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #path('', views.indexView, name="home"),
    path('', views.dashboardView, name="dashboard"),
    #path('logout/', include('login.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
]
