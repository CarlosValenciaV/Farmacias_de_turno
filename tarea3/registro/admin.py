from django.contrib import admin

# Register your models here.
from .models import Fecha

class FechaAdmin(admin.ModelAdmin):
#        fieldsets = [
#        (None,               {'fields': ['id']}),
#        ('informacion', {'fields': ['local'], 'classes': ['collapse']}),
#       (None,               {'fields': ['mes']}),
#        (None,               {'fields': ['dia']}),
#    ]
#comentado ya que al parecer que anulan con las propiedad display,filter,etc...        
    list_display = ('mes','dia',)
    list_filter = ('mes',)
    search_fields = ('dia',)
    ordering = ('dia',)
admin.site.register(Fecha,FechaAdmin)

from .models import Farmacia

class FarmaciaAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Informacion General', {'fields': ['local','local_direccion'], 'classes': ['collapse']}),
        ('Horarios',               {'fields': ['horario'], 'classes': ['collapse']}),
        ('Ubicacion',               {'fields': ['cod_region','nom_comuna'], 'classes': ['collapse']}),
    ]    
list_display = ('local',)
search_fields = ('local',)

admin.site.register(Farmacia,FarmaciaAdmin)

from .models import Region

class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom_region',)
    search_fields = ('nom_region',)

admin.site.register(Region,RegionAdmin)

from .models import Horarios

class HorariosAdmin(admin.ModelAdmin):
    list_display = ('hora_ini','hora_fin')
    list_filter = ('horario',)
   # search_fields = ('mes',)
#se considera innecesario este filtro
admin.site.register(Horarios,HorariosAdmin)

from .models import Comuna

class ComunaAdmin(admin.ModelAdmin):
    #necesario solo si quieres visualizar parte de la tabla
        fieldsets = [
        (None,               {'fields': ['nom_comuna']}),
        ('informacion', {'fields': ['nom_localidad'], 'classes': ['collapse']}),
    ]
search_fields = ('nom_comuna',)
list_display = ('nom_comuna',)

admin.site.register(Comuna,ComunaAdmin)
