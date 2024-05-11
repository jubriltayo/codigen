from django.shortcuts import render, redirect
from .models import Link
from django.http import HttpResponse

def home(request):
    return render(request, 'qrcode.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        instance = Link(name=name)
        instance.save()
        return HttpResponse(instance.qrcode.url)
