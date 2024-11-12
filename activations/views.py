from django.http import JsonResponse
from .utils import get_token_colors, get_activation_distribution

def token_coloring(request):
    tokens = request.GET.get('text', 'Hello World').split()
    colors = get_token_colors(tokens)
    return JsonResponse({"tokens": tokens, "colors": colors})

def activation_distribution(request):
    distribution = get_activation_distribution()
    return JsonResponse({"distribution": distribution})
