from django.urls import path
from . import views

urlpatterns = [
    path('token_attention/', views.token_attention, name='token_attention'),
]
