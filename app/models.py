from django.db import models

# Create your models here.
class usuariocliente(models.Model):
    id_cliente=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    correo=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)

class proyecto(models.Model):
    id_proyecto=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    fecha_de_publicacion=models.CharField(max_length=50)
    id_vendedor=models.ForeignKey(usuariocliente,on_delete=models.CASCADE)

class categoria(models.Model):
    id_categoria=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

class proyecto_categoria(models.Model):
    id_proyecto=models.OneToOneField(proyecto,on_delete=models.CASCADE )
    id_categoria=models.OneToOneField(categoria,on_delete=models.CASCADE)

class subir_proyecto(models.Model):
    id_subidaProyecto=models.BigAutoField(primary_key=True)
    id_cliente=models.ForeignKey(usuariocliente,on_delete=models.CASCADE)
    titulo_proyecto=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    repositorio=models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='directorio/')
    


    


    
