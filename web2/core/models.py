from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Balconista(models.Model):
    nome_usuario = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    nivel_acesso = models.IntegerField()

    def __str__(self):
        return self.nome_usuario


class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    lista_livros = models.ManyToManyField(Livro, through='PedidoLivro')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id}"


class PedidoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    data_remessa = models.DateField()

    def __str__(self):
        return f"Pedido do Cliente: {self.cliente}"


class PedidoFornecedor(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    data_recebimento = models.DateField()

    def __str__(self):
        return f"Pedido do Fornecedor: {self.fornecedor}"


class PedidoLivro(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
