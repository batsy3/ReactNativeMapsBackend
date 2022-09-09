from django.contrib import admin
from .models.coordinates import *

# Register your models here.


@admin.register
class CoordinateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'polygonCoordinates'
    )

admin.site.register(Area, CoordinateAdmin)
admin.site.register(PolygonList)
admin.site.register(LatLang)
