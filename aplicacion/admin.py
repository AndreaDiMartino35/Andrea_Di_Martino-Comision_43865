from django.contrib import admin
from .models import Cliente, Criadero, Tambo, Agricultor, Foto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Criadero)
admin.site.register(Tambo)
admin.site.register(Agricultor)
admin.site.register(Foto)
