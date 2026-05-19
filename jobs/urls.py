from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:id>/', views.job_detail, name='job_detail'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('jobs/<int:id>/apply/', views.apply_job, name='apply_job'),
]