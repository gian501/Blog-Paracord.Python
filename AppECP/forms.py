from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'encabezado', 'contenido', 'image','precio','category','fabricante']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'encabezado':forms.Textarea(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'fabricante':forms.Select(attrs={'class':'form-control'}),

	    	
    
        }





