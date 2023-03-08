from django import forms
from .models import Producto ,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__' #['nombre', 'encabezado', 'contenido', 'image','precio','category','fabricante']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'encabezado':forms.Textarea(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'fabricante':forms.Select(attrs={'class':'form-control'}),

	    	
    
        }


class PerfilFormulario (forms.ModelForm):
      

      class Meta:
        model = Profile
        fields ='__all__'

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña Antigua', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

