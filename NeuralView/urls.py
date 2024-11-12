from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to NeuralView! Use the /api/ endpoints for testing.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/models/', include('models.urls')),
    path('api/activations/', include('activations.urls')),
    path('api/attention/', include('attention.urls')),
    path('', home), 
]
