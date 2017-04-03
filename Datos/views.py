from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from .models import Persona

# Create your views here.
def index(request):
	if request.method == "POST":
		nombre = request.POST.get("nombre")
		apellido = request.POST.get("apellido")
		edad = request.POST.get("edad")

		obj_persona = Persona(nombre=nombre, apellido=apellido, edad=int(edad))
		obj_persona.save()

	template = loader.get_template('index.html')
	ctx = Context({})
	return HttpResponse(template.render(ctx, request))