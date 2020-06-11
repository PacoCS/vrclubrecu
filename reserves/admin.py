from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin

from .models import Reserva, Material, Sala

class MaterialInline(admin.StackedInline):
    model = Material
    extra = 3

class ReservaInline(admin.StackedInline):
    model = Reserva
    extra = 3


class ReservaAdmin(admin.ModelAdmin):

    exclude=[]
    list_display=('usuario_f','date','show_material')

class MyUserAdmin(UserAdmin):

    exclude=[]
    inlines = [ReservaInline]

class MaterialAdmin(admin.ModelAdmin):

    exclude=[]
    list_display=('sala_f','material_text')




class SalaAdmin(admin.ModelAdmin):

    exclude=[]
    inlines = [MaterialInline]


admin.site.register(Reserva,ReservaAdmin)
admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Sala,SalaAdmin)
# Register your models here.
