from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project-detail/', views.project_detail, name='project_detail'),
    path('project1/', views.project1_view, name='project1'),
]