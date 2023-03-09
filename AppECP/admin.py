from django.contrib import admin
from .models import Categorias, Producto, Contacto, Profile 
from .forms import ProductoFormulario

# Register your models here.


admin.site.register(Profile)
admin.site.register(Categorias)
admin.site.register(Producto)
admin.site.register(Contacto)
#admin.site.register(Carrito)