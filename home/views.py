from django.shortcuts import render
from .models import Telegram
# Create your views here.

def login(request):
    return render(request,'login.html')


def user_list(request):
    users = Telegram.objects.all()
    return render(request, 'index.html', {'users': users})
