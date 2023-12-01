from django.shortcuts import render
from .forms import Todo_form
from .models import *
# Create your views here.
def index(request):
    context={}

    todo_form=Todo_form()
    todo=Todo()
    context['todo_form']=todo_form
    return render(request,'index.html',context)