from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_activity_view, name='create_activity'),
    path('', views.create_activity_view, name = 'dashboard'),]