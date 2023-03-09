from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#Categorias
class Categorias (models.Model):
	nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	active = models.BooleanField(default=True, verbose_name='Activo')
	creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre
	
#Productos
class Producto(models.Model):
	nombre = models.CharField(max_length=250, verbose_name='Nombre')
	encabezado = models.TextField(verbose_name='Encabezado')
	contenido = models.TextField(verbose_name='Contenido')
	image = models.ImageField(default='users/cobra.png',upload_to='producto/', null=True, blank=True, verbose_name='Imagen')
	precio = models.FloatField()
	creacion = models.DateField(verbose_name='Fecha de creación')

	# Campos con relaciones
	category = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoría')
	fabricante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Fabricante')

	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'
		ordering = ['-creacion']

	def __str__(self):
		return self.nombre
	


#Contacto
opciones_consulta = [
	[0, "Consulta"],
	[1, "Reclamo"],
	[2, "sugerencia"]
]

class Contacto (models.Model):
	nombre = models.CharField(max_length=40)
	correo = models.EmailField()
	tipo_consulta = models.IntegerField(choices=opciones_consulta)
	mensaje = models.TextField()
	notificacion = models.BooleanField()


	def __str__(self):
		return self. nombre

#Profile
class Profile(models.Model):
	user = models. OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(default='users/image_user.png', upload_to='users/', null=True, blank=True)
	biografia = models.TextField(max_length=400, null=True, blank=True)


	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
		ordering = ['-id']

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)






#Carrito
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")
    total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
class Carrito_item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")






