from django.urls import path
from .views import *
from AppECP import views

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('perfil/', perfil, name='perfil'),
    path('aboutus/', aboutus, name='aboutus'),
    path('busquedaProducto/', busquedaProducto, name= "busquedaProducto"),
    path('usuarioEditar/', editar_usuario, name="usuarioEditar"),
    path('contacto/', contacto, name='contacto'),
    path('perfilEditar/', editar_perfil, name='perfilEditar'),
   
    path('producto/list', views.ProductoListView.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetailView.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreateView.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdateView.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDeleteView.as_view(), name='Delete'),
]