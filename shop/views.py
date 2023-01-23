from django.shortcuts import render
from shop.models import About

# Create your views here.
def index(request):
    info = About.objects.all()
    return render(request, 'main.html', {'info':info})