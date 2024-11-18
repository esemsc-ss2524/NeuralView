from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# View to render the index (welcome) page
def home(request):
    return render(request, 'index.html')  # Render index.html as the welcome page

# View for the attention visualization page
def visualize_attention(request):
    return render(request, 'visualize_attention.html')  # Render attention visualization page

# View for the text generation with attention visualization (beta) page
def generate_and_visualize(request):
    return render(request, 'generate_and_visualize.html')  # Render text generation page

# Define the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/models/', include('models.urls')),
    path('api/activations/', include('activations.urls')),
    path('api/attention/', include('attention.urls')),
    path('', home, name='home'),  # Default to the index.html welcome page
    path('visualize-attention/', visualize_attention, name='visualize_attention'),
    path('generate-and-visualize/', generate_and_visualize, name='generate_and_visualize'),
]
