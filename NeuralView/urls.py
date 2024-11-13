from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # Add this import for rendering templates

# View to render the index page
def home(request):
    return render(request, 'index.html')  # Render index.html from the templates folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/models/', include('models.urls')),
    path('api/activations/', include('activations.urls')),
    path('api/attention/', include('attention.urls')),
    path('', home),  # This will render the index.html by default
]
