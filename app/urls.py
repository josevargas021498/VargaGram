from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.modelFormUpload, name='base'),
    path('feed/', views.feedFunction, name='feed'),
]
