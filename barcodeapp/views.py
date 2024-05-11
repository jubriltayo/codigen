from django.shortcuts import render, redirect, reverse
from uuid import uuid4
from .models import Product
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'barcode.html')

def create(request):
    if request.method == 'POST':
        barcode_id = str(uuid4())[:5]
        name = request.POST['name']
        country_id = request.POST['country_id']
        manufacturer_id = request.POST['manufacturer_id']
        number_id = request.POST['number_id']
        instance = Product(name=name, barcode_id=barcode_id, country_id=country_id, manufacturer_id=manufacturer_id, number_id=manufacturer_id)
        instance.save()
        return HttpResponse(instance.barcode.url)
