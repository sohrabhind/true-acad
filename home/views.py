from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello this is home page of Revision')

def about(request):
    return HttpResponse('About Page')