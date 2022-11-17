from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from.models import App
from .serializers import *
 
@csrf_exempt
# Create your views here.

def simpleApp (request):
    if request.method == 'GET':
        appnow = App.objects.all()
        serializers = AppSerializers (appnow, many=True)
        return JsonResponse (serializers.data, safe =False)

    elif request.method == 'POST':
        data1 = JSONParser().parse(request)
        serializers = AppSerializers (data=data1)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse (serializers.data, status=201)
        return JsonResponse (serializers.errors, status=400)        