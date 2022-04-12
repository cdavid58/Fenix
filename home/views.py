from django.shortcuts import render
from .models import *
from conductores.models import Coche

def Home(request):
	if 'img_fondo' in request.session:
		del request.session['img_fondo']
		del request.session['img_about']
	ns = Nuestros_Servicio.objects.last()
	about = Nosotro.objects.last()
	n_coches = Coche.objects.all()
	request.session['img_fondo'] = Modificaciones.objects.last().img_fondo_principal.url
	request.session['img_about'] = Modificaciones.objects.last().img_nuestros_servicios_fondo.url
	return render(request,'index.html',{'ns':ns,'no':about,'n_coches':len(n_coches)})