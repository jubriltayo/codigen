from django.shortcuts import render, redirect
from uuid import uuid4
from .models import Url
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        link_id = str(uuid4())[:5]
        instance = Url(link_id=link_id, link=url)
        instance.save()
        return HttpResponse(link_id)

def shortened_url(request, pk):
    instance = Url.objects.get(link_id=pk)
    return redirect(instance.link)
