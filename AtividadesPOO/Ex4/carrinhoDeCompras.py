class carrinho_de_compras():

    def __init__(self):
        self.pdt_selecionado = []
        self.preco = []

    def adicionar(self, produto, preco : float):
        self.pdt_selecionado.append(produto)
        self.preco.append(preco)

    def valor_carrinho(self):
        return sum(self.preco)

    def mostrar_itens(self):
        if not self.pdt_selecionado:
            print('Carrinho vazio')
        else:
            print('Carrinho: ')
            for produto, preco in zip(self.pdt_selecionado, self.preco):
                print(f'{produto}: R${preco:.2f}')

carrinho = carrinho_de_compras()

carrinho.adicionar('Agua',2.00)
carrinho.adicionar('Chocolate',5.00)
carrinho.adicionar('Refrigerante',10.82)

carrinho.mostrar_itens()

total = carrinho.valor_carrinho()
print(f'Total da compra de: R${total:.2f}')