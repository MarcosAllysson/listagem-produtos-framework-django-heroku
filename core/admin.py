from django.contrib import admin
from .models import Produto, Cliente


# Exibindo outros dados na tela administrativa
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


# Register your models here.
admin.site.register(Produto, ProdutosAdmin)
admin.site.register(Cliente, ClientesAdmin)
