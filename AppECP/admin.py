from django.contrib import admin
from .models import Profile, Categorias, Producto

# Register your models here.
admin.site.register(Profile)
admin.site.register(Categorias)
admin.site.register(Producto)