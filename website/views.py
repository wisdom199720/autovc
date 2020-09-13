from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def home(request):

    prods = product.objects.all()

    return render(request, 'index.html', {'prods':prods})

