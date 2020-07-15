from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre_depa=models.CharField(max_length=20)

class Municipio(models.Model):
    nombre_muni=models.CharField(max_length=30)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE, default=None)

class Ubicacion(models.Model):
    id_ubicacion=models.CharField(primary_key=True,max_length=5)
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE,default=None)

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=10)

class Problema(models.Model):
    descripcion=models.CharField(max_length=100)
    sector=models.CharField(max_length=20)
    fecha=models.DateField()
    ubicacion=models.ForeignKey(Ubicacion, on_delete=models.CASCADE,default=None)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,default=None)

    