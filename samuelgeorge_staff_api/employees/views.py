from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def manager_api(request):
    if request.method == 'GET':
        manager_role = employees.models.Manger.get_role()
        return JsonResponse(manager_role, safe=False)

def intern_api(request):
    if request.method == 'GET':
        intern_role = employees.models.Intern.get_role()
        return JsonResponse(intern_role, safe=False)
