from django.shortcuts import render
from shop.models import category


# Create your views here.

def index(request):
    show = category.objects.all()
    return render(request, 'main.html', {'show': show})


