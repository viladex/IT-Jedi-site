from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def main(request):
    return render(request, 'main/about.html')

def state1(request):
    return render(request, 'main/states1.html')

def state2(request):
    return render(request, 'main/states2.html')

def state3(request):
    return render(request, 'main/states3.html')

def chapterFramework(request):
    return render(request, 'main/chapterFramework.html')

def chapterProgramLang(request):
    return render(request, 'main/chapterProgramLang.html')

def chapterDatabase(request):
    return render(request, 'main/chapterDatabase.html')

def chapterWeb(request):
    return render(request, 'main/chapterWeb.html')

def tegPython(request):
    return render(request, 'main/tegPy.html')

def tegJava(request):
    return render(request, 'main/tegJa.html')

def tegJavaScript(request):
    return render(request, 'main/tegJaSc.html')

def tegPHP(request):
    return render(request, 'main/tegPhp.html')

def contact(request):
    return render(request, 'main/contact.html')

