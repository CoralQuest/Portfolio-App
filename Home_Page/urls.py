from django.urls import path
from . import views
from calculator.views import calculator_view

urlpatterns = [
    path('', views.home, name='home'),
    path('project-detail/', views.project_detail, name='project_detail'),
    path('project1/', views.project1_view, name='project1'),
    path('calculator/', calculator_view, name='calculator'),
]