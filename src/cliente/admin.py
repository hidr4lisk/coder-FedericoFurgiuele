from django.contrib import admin

# Register your models here.
from .models import Cliente, Pais

"""admin.site.register(Cliente)
admin.site.register(Pais) """


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacimiento', 'pais_origen')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')
    list_filter = ('pais_origen',)
    date_hierarchy = 'nacimiento'
