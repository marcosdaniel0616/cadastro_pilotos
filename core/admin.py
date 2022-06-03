from django.contrib import admin
from core.models import Piloto


@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'altura', 'slug', 'criado', 'modificado', 'ativo')
