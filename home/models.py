from django.db import models

class Nuestros_Servicio(models.Model):
	nombre = models.CharField(max_length = 50)
	descripcion = models.TextField()

class Nosotro(models.Model):
	descripcion = models.TextField()

class Modificaciones(models.Model):
	img_fondo_principal = models.ImageField(upload_to="Img_Fondo" )
	img_nuestros_servicios_fondo = models.ImageField(upload_to = 'our_service',null=True)

