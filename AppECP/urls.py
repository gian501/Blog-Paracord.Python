from django.urls import path
from .views import home, products, register, aboutus


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('aboutus/', aboutus, name='aboutus'),
]