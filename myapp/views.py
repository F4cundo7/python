from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError 
from .forms import Obraform
from .models import Obra
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == 'GET':        
        return render(request, 'login.html', {
        'form' : UserCreationForm
    })
    else:
        if request.POST['contraseña1'] == request.POST['contraseña2']:
            try:                
                user= User.objects.create_user(username=request.POST['usuario'],password=request.POST['contraseña1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'login.html', {
                    'form' : UserCreationForm,
                    'error' : 'Nombre de usuario ya existe'
                })
        return render(request, 'login.html', {
            'form' : UserCreationForm,
            "error" : 'Nombre de usuario ya existe'
    })
    
    
def task(request):
    obras = Obra.objects.all()
    return render(request, 'task.html',{'obras': obras})

def crear_obra(request):
    if request.method == 'GET':
        return render(request, 'crear_obra.html',{
        'form': Obraform
        })
    else:
        try:
            form = Obraform(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('home')
        except ValueError:
            return render(request, 'crear_obra.html', {
                'form': Obraform,
                'error': 'Porfavor intenta otro dato'
            })
        
def tasks_search(request):
    
    if request.method == 'GET':
        search_term = request.GET.get('id')
        
        if search_term :
            obras = Obra.objects.filter(id__exact=search_term)
        else: 
            obras=Obra.objects.all()
    return render(request, 'tasks.html', {'obras': obras}) 
    
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user= authenticate(
            request, username=request.POST ['usuario'], password=request.POST['contraseña1'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'El Usuario o la Contraseña es incorrecta '
        })
            
        else:
            login(request, user)
            return redirect('home')
        
 
    