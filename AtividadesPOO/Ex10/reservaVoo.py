class Passageiro():
    def __init__(self, nome, num_pass):
        self.nome = nome
        self.num_pass = num_pass

class Voo():
    def __init__(self, voo, origem, destino, capacidade : int):
        self.voo = voo
        self.origem = origem
        self.destino = destino
        self.capacidade = capacidade
        self.reservas = []

    def lotado(self):
        return len(self.reservas) >= self.capacidade

    def mostrar_reservas(self):
        return [reserva for reserva in self.reservas]

    def reservar_assento(self, passageiro):
        if not self.lotado():
            nova_reserva = Reserva(passageiro, self)
            self.reservas.append(nova_reserva)
            return nova_reserva
        else:
            print('Voo lotado')

    # def exibir_voo(self):
    #     print('--- Voo ---\n'
    #           f'Numero do Voo: {self.voo}\n'
    #           f'Origem: {self.origem}\n'
    #           f'Destino: {self.destino}')

class Reserva():
    def __init__(self, passageiro, voo):
        self.passageiro = passageiro
        self.voo = voo


passageiro1 = Passageiro('Matheus', '5555')
passageiro2 = Passageiro('Roberto', '22222')

voo1 = Voo('TAM', 'Santa Catarina','Rio de Janeiro', 10)
voo2 = Voo('Boing', 'Santa Catarina','Rio Grande do Sul', 8)

reserva1 = voo1.reservar_assento(passageiro1)
reserva2 = voo1.reservar_assento(passageiro2)
reserva3 = voo1.reservar_assento(passageiro1)

print('Reservas do Voo TAM:')
for reserva in voo1.mostrar_reservas():
    print(f'Passageiros: {reserva.passageiro.nome}')

print('\nReservas do Voo Boing:')
for reserva in voo2.mostrar_reservas():
    print(f'Passageiros: {reserva.passageiro.nome}')
