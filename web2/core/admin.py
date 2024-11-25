from django.contrib import admin
from .models import PedidoLivro, PedidoFornecedor, PedidoCliente, Pedido, Balconista, Cliente, Livro, Fornecedor

admin.site.register(PedidoFornecedor)
admin.site.register(PedidoLivro)
admin.site.register(PedidoCliente)
admin.site.register(Pedido)
admin.site.register(Balconista)
admin.site.register(Cliente)
admin.site.register(Livro)
admin.site.register(Fornecedor)
