from django.urls import path
from . import views

urlpatterns = [
    path('token_coloring/', views.token_coloring, name='token_coloring'),
    path('distribution/', views.activation_distribution, name='activation_distribution'),
    #########
    path('generate_with_attention/', views.generate_with_attention, name='generate_with_attention'),
]
