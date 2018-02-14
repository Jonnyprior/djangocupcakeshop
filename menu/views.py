from django.shortcuts import render
from . import models

def cupcake_list(request):
	return render(request,"menu/list.html",{})

# Create your views here.
