from django.contrib import admin
from .models import ActivosModel

admin.site.site_header = 'Welcome to TechStock'
admin.site.index_title = 'My Inventory Lis'
admin.site.site_title = 'Inventory'

data_tuple = (
    'codigo_activo', 'laboratorio', 'tipo',
    'marca', 'estado', 'estado_uso',
    'observacion', 'imagen',
)


@admin.register(ActivosModel)
class ActivoosAdmin(admin.ModelAdmin):
    fields, list_display = data_tuple, data_tuple
