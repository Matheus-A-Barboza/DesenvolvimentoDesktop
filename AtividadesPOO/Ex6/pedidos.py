class pedidos():
    def __init__(self, numero : int, data):
        self.numero = numero
        self.data = data
        self.itens = []

    def adicionar(self, pedido, item):
        self.itens.append(pedido)
        self.itens.append(item)

    def mostrar_itens(self):
        if not self.itens:
            print('Pedido vazio')
        else:
            print('Pedido: ')
            for pedido in zip(self.itens):
                print(f'{self.itens} Data: {self.data}')
                break

pedido = pedidos(1,'15/08/2023')
pedido.adicionar(1, 'Chinelo')
pedido.adicionar(2,'Camisa')
pedido.mostrar_itens()