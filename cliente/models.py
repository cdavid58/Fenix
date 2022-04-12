from django.db import models


class Cliente(models.Model):
	nombre = models.CharField(max_length = 40)
	telefono = models.CharField(max_length=10)
	bloqueado = models.BooleanField(default = False)

	def __str__(self):
		return self.nombre