from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def index(request):

    data = {'foo': 'bar', 'hello': 'world'}

    return HttpResponse(json.dumps(data), content_type='application/json')


def sagas(request):
