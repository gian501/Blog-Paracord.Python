from django.urls import path
from .views import home, products, register, aboutus, ProductoUpdateView 
from AppECP import views

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('aboutus/', aboutus, name='aboutus'),

      path('producto/list', views.ProductoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetailView.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreateView.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdateView.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDeleteView.as_view(), name='Delete')
]