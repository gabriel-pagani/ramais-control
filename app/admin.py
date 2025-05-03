from django.contrib import admin
from .models import Ramais


@admin.register(Ramais)
class RamaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramal', 'setor', 'maquina')
