from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def main(request):
    return render(request, 'mainPage/index.html')