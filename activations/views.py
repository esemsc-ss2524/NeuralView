from django.http import JsonResponse
from .utils import generate_tokens_with_attention
from .utils import get_token_colors, get_activation_distribution

def token_coloring(request):
    tokens = request.GET.get('text', 'Hello World').split()
    colors = get_token_colors(tokens)
    return JsonResponse({"tokens": tokens, "colors": colors})

def activation_distribution(request):
    distribution = get_activation_distribution()
    return JsonResponse({"distribution": distribution})


##################################


def generate_with_attention(request):
    initial_phrase = request.GET.get('text', 'Hello')
    num_tokens = int(request.GET.get('num_tokens', 1))

    try:
        results = generate_tokens_with_attention(initial_phrase, num_tokens)
        return JsonResponse({"results": results})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
