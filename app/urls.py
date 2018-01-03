from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.model_Form_Upload, name='base'),
    path('feed/', views.feed_Function, name='feed'),
]
