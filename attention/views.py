from django.shortcuts import render

from django.http import JsonResponse
from .utils import get_token_attention

def token_attention(request):
    tokens = request.GET.get('text', 'Hello World').split()
    attention = get_token_attention(tokens)
    return JsonResponse({"tokens": tokens, "attention": attention})
