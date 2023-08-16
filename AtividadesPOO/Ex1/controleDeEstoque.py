class Produto():
    def __init__(self, nome, preco : float, qnt_estoque : int):
        self.nome = nome
        self.preco = preco
        self.qnt_estoque = qnt_estoque

    def adicionar(self, adicionar):
        produto.qnt_estoque += adicionar

    def remover(self, remover):
        produto.qnt_estoque -= remover

    def valor_estoque(self):
        valor_total = 0
        valor_total = self.preco * self.qnt_estoque
        print(f'Valor de estoque: R${valor_total}\n'
              f'Quantidade de {produto.nome} em estoque: {produto.qnt_estoque}')

produto = Produto('Bolacha',2, 100)
produto.adicionar(8)
produto.remover(1)
produto.valor_estoque()