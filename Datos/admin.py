from django.contrib import admin

from .models import Persona

@admin.register(Persona)
class adminPersona(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'apellido', 'edad']
	list_filter = ['id', 'nombre', 'apellido', 'edad']
	search_fields = ['nombre']