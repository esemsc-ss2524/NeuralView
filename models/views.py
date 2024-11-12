from django.shortcuts import render

from django.http import JsonResponse
from .utils import load_model_util

def load_model(request):
    success = load_model_util()
    return JsonResponse({"status": "model loaded" if success else "error"})
