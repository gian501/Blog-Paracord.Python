from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto, Categorias, User ,Carrito, Carrito_item
from .forms import ProductoFormulario
from django.urls import reverse_lazy
#from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages


# Create your views here.




def home(request):
    return render(request, 'AppECP/home.html')

@login_required
def products(request):
    producto = Producto.objects.all()
    page= request.GET.get('page', 1)

    try:
        paginator = Paginator(producto, 1)
        producto = paginator.page(page)
    except:
        raise Http404


    return render(request, 'AppECP/products.html', {'producto':producto, 'paginator':paginator})

#Listado de Producto
class ProductoList(ListView):
    model = Producto
    template_name = "AppECP/producto_list.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "AppECP/producto_detalle.html"

#Crear Producto
#@permission_required('AppECP.add_producto')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoFormulario

    def form_valid(self, form):
        form.instance.fabricante = self.request.user
        return super().form_valid(form)

    success_url = 'products'

#Edición del Producto
#@permission_required('AppECP.change_producto')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoFormulario
    success_url = "/Core/producto/list"

    def form_valid(self, form): #esto es que el editor pueda editar el producto
        form.instance.fabricante = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Detail', args=[self.object.id]) + '?ok'

#Eliminar un Producto
#@permission_required('AppECP.delete_producto')
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = "/AppECP/producto/list"

#Registro de usuario
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




def busquedaProducto(request):
    texto_de_busqueda = request.GET["texto"]
    productosPorNombre = Producto.objects.filter(nombre__icontains = texto_de_busqueda).all()
    productos = productosPorNombre 
    return render(request, 'AppECP/busquedaProducto.html',{'productos' : productos,'texto_buscado' : texto_de_busqueda,'titulo_seccion' : 'Productos que contienen','sin_productos' : 'No hay producto de la categoria ' + texto_de_busqueda})




def carrito_index(request):
    categorias = Categorias.objects.all()
    usuario_logeado = User.objects.get(username=request.user)
    productos = Carrito.objects.get(usuario=usuario_logeado.id).items.all()

    carrito = Carrito.objects.get(usuario=usuario_logeado.id)
    nuevo_precio_Carrito = 0
    for item in carrito.items.all():
        nuevo_precio_Carrito += item.producto.precio
    carrito.total = nuevo_precio_Carrito
    carrito.save()

    return render(request, '"AppECP/carrito_compras.html"', {
        'categorias' : categorias,
        'usuario' : usuario_logeado,
        'items_carrito' : productos
    })


def carrito_save(request):
    if request.method == 'POST':
        producto = Producto.objects.get(id=request.POST['producto_id'])
        usuario_logeado = User.objects.get(username=request.user)

        # Agrego producto al carrito
        carrito = Carrito.objects.get(usuario=usuario_logeado.id)
        item_carrito = Carrito_item()
        item_carrito.carrito = carrito
        item_carrito.producto = producto
        item_carrito.save()

        # Sumo el precio del producto al carrito
        carrito.total = producto.precio + carrito.total
        carrito.save()
        messages.success(request, f"El producto {producto.titulo} fue agregado al carrito")
        return redirect("AppECP/carrito_compras.html")

    else:
        return redirect("AppECP/carrito_compras.html")

def carrito_clean(request):
    usuario_logeado = User.objects.get(username=request.user)
    carrito = Carrito.objects.get(usuario=usuario_logeado.id)
    carrito.items.all().delete()
    carrito.total = 0
    carrito.save()
    return redirect("AppECP/carrito_compras.html")

def item_carrito_delete(request, item_carrito_id):
    item_carrito = Carrito_item.objects.get(id=item_carrito_id)
    carrito = item_carrito.carrito
    
    # Vuelvo a calcular el precio del carrito
    nuevo_precio_Carrito = 0 - item_carrito.producto.precio
    for item in carrito.items.all():
        nuevo_precio_Carrito += item.producto.precio

    # Realizo los cambios en la base de datos
    carrito.total = nuevo_precio_Carrito
    item_carrito.delete()
    carrito.save()
    return redirect("AppECP/carrito_compras.html")
    
