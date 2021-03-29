from django.urls import path

from . import views


urlpatterns = [
    path('', views.upload_file_class, name='upload_file'),
    path('generate', views.generate_file, name='generate_file'),
    path('info', views.response_info, name='info'),
]
