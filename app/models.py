from django.db import models

# Create your models here.
class usuariocliente(models,Model):
    id_cliente=models.BigAutoFieldAutoField(primary_key=True)
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    correo=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)

class proyecto(models,model):
    id_proyecto=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    fecha_de_publicacion=models.CharField(max_length=50)
    id_vendedor=models.ForeignKey(usuariocliente,on_delete=models.CASCADE)

class categoria(models,model):
    id_categoria=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
        


    
