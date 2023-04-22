# E-ComerceParacord


Procedimos a la creación de un proyecto, blog con la posibilidad de extension a E-Comerce. Comenzamos con la creación del proyecto y la instalación de la aplicación.

El video sera subido a google drive ya que tiene mas de nueve minutos.

https://drive.google.com/file/d/17saZcvfo_uDlcCap9R7-y-Q9v-QyzMDb/view?usp=sharing


Modelos:

1.  Categorías:Realice la creación de modelos en el cual nos basamos en un modelo de  producto, con sus respectivas categorías, ya que como está orientado al Paracord, las categorías no sirven para crear las distintas disposiciones en la utilización del mismo. Como es en el caso que a través del Admin creamos las categorías de :
            A.Pulseras 
             B. Nudos 
             C.Accesorios 
              D. Mascotas 
2. Agregamos el modelo Profile para poder editar los usuarios, y de esta manera, poder colocarles imágenes y una descripción.
3. Si bien no creado en este orden. Desarrolle un modelo Producto cumpliendo las consignas del trabajo colocándole los atributos de nombre, encabezado, contenido, precio, fecha de creación. Llegamos a través de la clave foránea los atributos de categoría para clasificar los productos categorias y fabricante.
4. Creamos una clase Contacto en el cual le pusimos las opciones de consulta: Consulta, Reclamo, sugerencia con el objetivo de qué terceros puedan comunicarse y los mensajes quedarán guardados en el en el  admin


Formularios:
Mediante el uso de Django como Framework utilizamos herramientas para crear formularios :

A. CustomUserCreationForm  importamos el modelo USER  de Django para realizar un formulario de registro que tiene las categorías de: 
1. Username 
2. Nombre
3. Apellido
4. Email
5. Contraseña
6. Confirmación de contraseña
El cual importamos desde el mismo Django y nos sirvieron para crear el login y el Register.

B. ProductoFormulario: un formulario creado también utilizando las herramientas de Django con el objeto de manejar los productos que podríamos ver en detalle, crear modificar, eliminar y listar. Esto es igual que seria con los post nada mas que orientado a productos de Paracord, cuyas categorías son:
1. Nombre
2. Encabezado
3. Descripción
4. Image = imagen
5. Categoría= que a través de la clave foránea podríamos utiliza
6.  Precio (para su futura incorporación al e-comercie y darle al usuario que vea el blog una referencia de precio del producto)
7. Fabricante (persona que agrego el producto )
8. Y fecha de creación

C. UserEditFormulario: un formulario creado con el objetivo de poder modificar el formulario de User de Django por lo cual utilizaría las mismas categorías que el formulario de usuario

D. ContactoFormulario: En el cual creamos un formulario basados en los campos de:
1. Nombre 
2. Correo
3. Tipo de consulta ( las cuales fueron definidas en el models
4. Mensaje 
5. Notificación
Éste formulario sirve para dejar mensajes dentro de la página web que se puede ver a través del Admin.

E. PerfilFormulario: este formulario se basa en el modelo de profile, con el objetivo de poder agregar, editar y borrar la foto de perfil y una descripción.

Views:

Dentro de las vistas, definimos las distintas funciones que tendrá nuestra página web entre las cuál es esta:
1. Home : la cual es la pagina de inicio
2. Products: la cual es um tipo de catalogo que nos permite ver todos los productos creados. Acá se creó paginador con el objeto de que en la pagina solo se muestren 3 productos.
3. Aboutus: es lo que nos renderiza una pagina que habla de nosotros
4. Contacto: que es lo que nos permite dejar mensajes 
5. Y la búsqueda de productos por nombre que nos permitirá dentro de la pagina productos encontrarlos más fácilmente.    
CRUD:
1. Producto ListView: que nos permite sólo a los Super usuarios, listar todos los productos con una pequeña descripción para poder ver, borrar y editar.
2. Producto DetailView: a través de esta podemos ver en detalle en el templete creado con el nombre producto_detalle.html el detalle de cada producto. Como ser la imagen, fabricante, categoría, foto, precio.
3. Producto CreateView: esto nos permite a través de un formulario creado a través de Krispy que es una función que nos permite renderizar de mejor manera el formulario, crear un producto con todos los atributos que provienen del formulario creado basado en el modelo producto. Esto esta en el témplate producto_form.html
4. Producto UpdateView: esto nos permite a través del mismo formulario de creación editar el producto.
5. Producto DeleteView: esto nos permitiría a los Super usuarios ya que se pusieran permisos para eso, a través del listado eliminar los productos creados y nos redirigiría una vista que nos preguntaría si realmente deseamos eliminarlos la cual es producto_confirm_ delete.html

6.Register: a través de los formularios creados podríamos registrar un usuario nuevo para el cual se Utilizó CrispyForms para mejorarlo y posteriormente que el usuario pueda loquearse: estos están en dos templates: en una carpeta llamada registration están el login y el register. Esto nos permitirá estar registrados como usuarios dentro de la base de datos y poder ingresar a la página para ver los productos. En el settings redirigimos Logout o salir de la sesión para el Home.

7. Editar_usuario: esto nos permitirá a través del mismo formulario de usuario modificar el nombre, el apellido y el e-mail. Si llega esto a través del témplate perfil.html, el cual Nos muestra el perfil de usuario , con su nombre foto y descripción provenniente de los modelos de usuario y perfil. 
8. Editar_perfil: esto nos permite agregar, cambiar y eliminar la foto y biografía del usuario. se llega a  el atravez del témplate perfil.html opción modificar imagen.


Imágenes : se realizaron configuraciones en el setting para poder introducir y ver imágenes de perfil ya que la imagen de los productos solo pueden ser agregadas por el súper usuario. Las imágenes quedaran guardas en la carpeta Media, ya sea en la subcarpeta Productos o Users
Las imágenes de los productos solo pueden ser agregadas desde el panel de Administracion o admin.

Se realizo un requiremets.txt Para especificar al instalar que necesita para hacer correr el programa  lo cual es :
Python:
Django:
Crispy_forms.
Pillow


Utilización de la pagina :
Al hacer correr el servidor con el comando Python3 manage.py runserver con la puerta que prefieran, se desplegará la página de inicio que fue renderizada a través del témplate home.html. Aquí veremos el nombre de la empresa GV-Paracord y una barra de navegación con las opciones de:
1.Home : nos lleva al inicio
2.Aboutus: cuenta sobre la empresa, la página, el producto y nos permite ver las credenciales de contacto
3.Productos: para lo cual necesitaríamos estar registrados, si no lo  estamos, nos regirá al formulario de logueo. Al haber completado este paso nos llevara al témplate products.html el cual renderiza todos los productos creados(solo hay 3 por pagina). Nos mostrara una foto, nombre, precio y un “Ver detalle” que nos llevara al detalle de cada producto.
Si ingresamos podremos ver las características del modelo de producto y nos da la opción de volver al catalogo y de comprar.
La pagina de producto en su inicio tiene una barra de búsqueda que si encuentra el producto o productos nos lo muestra y sino nos da un mensaje de no hay resultado.
4.Contacto : nos lleva a una pagina donde encontramos un formulario que nos permite enviar un mensaje que quedara guardado en la base de datos.
5.Ingresar si no estamos registrados nos lleva al formulario de logueo. 
6. Registrarse nos llevara al formulario de registro
7.Una vez ingresados si estamos registrados nos aparecerá el nombre del usuario por ejemplo “Gian_5555” presionándolo nos dará opciones:

1. Si es Superusuario:
A. Listar productos: que nos permite ver todos los productos creados, sus nombres y la posibilidad de 
.Ver(muestra el detalle del producto) 
.Modificar(nos lleva al formulario de modificación que es el mismo que el de creación) 
.Borrar(nos permite borrrar productos y nos envía a una pagina de confirmación)

Y tiene todas las otras opciones de usuarios comunes

2. Su es un usuario común :
B.Agregar producto: que nos lleva al formulario de creacion de productos(podremos ingresar una foto pero no aparecerá, solo desde el admin se podrá administrar las imagenes)
C. Perfil: nos lleva al témplate perfil que nos permite ver: una foto del perfil, el nombre de usuario, el nombre, el apellido, el e-mail y una descripcion. Que de ser nueva podemos agregarla junto a una nueva imagen de perfil con la opción de “modificar imagen usuario”.
También tenemos la opción “Modificar datos de usuario” que nos lleva al formulario para modificar nombre, apellido y email, debiendo confírmala con nuestra contraseña.
D. Cerrar sesión: que nos redigira como lo definimos en el settings. Del programa a Home. 




