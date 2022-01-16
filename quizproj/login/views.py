from django.shortcuts import render
from django.http import HttpResponse


def printOut(request):
    return render(request, 'login_template.html', {"name":"Ismet"})

def print(request):
    if request.GET.get('LoginBtn'):
        return render(request, 'login_template.html', {"statement":"Button clicked."})
# Create your views here.
