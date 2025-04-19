from django.shortcuts import render

# Create your views here.

from .models import Projects

def home(request):
    data = Projects.objects.all().order_by('-id')[:250]
    return render(request, 'home.html', {'data': data})

