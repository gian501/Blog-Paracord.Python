from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
#from .models import Producto
#from django.http import HttpResponse
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy

# Create your views here.




def home(request):
    return render(request, 'AppECP/home.html')

@login_required
def products(request):
    #producto = Producto.objects.all()
    return render(request, 'AppECP/products.html')#, {'producto':producto}

#def exit(request):
    #logout(request)
    #return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', data)

def aboutus(request):
    return render(request, 'AppECP/aboutus.html')