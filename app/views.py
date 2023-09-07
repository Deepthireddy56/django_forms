from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def djforms(request):
    SFO=Studentform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'djforms.html',d)