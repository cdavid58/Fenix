from django.db import models

class Conductor(models.Model):
	nombre = models.CharField(max_length = 40)
	documento_identidad = models.IntegerField(unique = True)
	email = models.EmailField()
	telefono = models.CharField(max_length = 10)
	activo = models.BooleanField(default = False)
	bloqueado  = models.BooleanField(default = False)

	def __str__(self):
		return self.nombre

class Coche(models.Model):
	color = models.CharField(max_length = 30)
	placa = models.CharField(max_length = 10)
	maletero = models.BooleanField(default = False)
	dos_puertas = models.BooleanField(default = False)
	cuatro_puertas = models.BooleanField(default = False)
	conductor = models.ForeignKey(Conductor,on_delete = models.CASCADE)

	def __str__(self):
		return self.conductor.nombre


class Documento(models.Model):
	documento_identidad = models.ImageField(upload_to = "Document_Driver")
	veguro_vehicular = models.ImageField(upload_to = "Document_Driver")
	licencia = models.ImageField(upload_to = "Document_Driver")
	conductor = models.ForeignKey(Conductor,on_delete = models.CASCADE)

	def __str__(self):
		return self.conductor.nombre	

