from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto
from .forms import ProductoFormulario
from django.urls import reverse_lazy
#from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.




def home(request):
    return render(request, 'AppECP/home.html')

@login_required
def products(request):
    producto = Producto.objects.all()
    return render(request, 'AppECP/products.html', {'producto':producto})

#Listado de Producto
class ProductoList(ListView):
    model = Producto
    template_name = "AppECP/producto_list.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "AppECP/producto_detalle.html"

# Crear Producto
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoFormulario

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = "/AppECP/producto/list"

# Edición del Producto
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoFormulario
    success_url = "/Core/producto/list"

    def form_valid(self, form): #esto es que el editor pueda editar el producto
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Detail', args=[self.object.id]) + '?ok'

# Eliminar un Producto
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = "/AppECP/producto/list"

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