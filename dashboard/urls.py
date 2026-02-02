from django.urls import path
from . import views

urlpatterns = [
    path('', views.ngo_list_view, name='ngo_list'),
    path('create/', views.create_activity_view, name='create_activity'),
    path('update/<int:pk>/', views.update_activity_view, name='update_activity'),
    path('toggle/<int:pk>/', views.toggle_activity_status_view, name='toggle_activity'),
    path('dashboard/', views.ngo_list_view, name='dashboard'), # 兼容旧命名
]