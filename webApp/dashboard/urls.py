from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from . import views  # pylint: disable=relative-beyond-top-level


urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('add/', views.addPatient, name="add_patient"),
    path('scans/', views.scans, name="scans"),
    
]
