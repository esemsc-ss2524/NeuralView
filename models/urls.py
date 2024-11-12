from django.urls import path
from . import views

urlpatterns = [
    path('load', views.load_model, name='load_model'),
]
