from django.urls import path
from . import views

urlpatterns = [
    path('', views.response_info, name='home'),
    path('post/', views.upload_file, name='create_post'),
    path('generate', views.generate_file, name='generate_file'),
]
