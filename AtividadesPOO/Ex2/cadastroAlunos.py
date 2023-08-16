class Alunos():
    def __init__(self, nome, idade : int):
        self.nome = nome
        self.idade = idade

    def adicionar(self, adicionar, materias : list):
        materias.append(adicionar)

    def remover(self, remover, materias : list):
        materias.remove(remover)

    def mostrar_discplina(self, materias : list):
        print(f'Aluno: {self.nome} | Idade: {self.idade}\n'
              f'Disciplinas: {materias}')

materias = ['Arquitetura de Redes', 'Arquitetura de Soft.', 'Eng. de Software']

aluno = Alunos('Matheus', 20)
aluno.adicionar('Des. Desktop', materias)
aluno.remover('Arquitetura de Redes', materias)
aluno.mostrar_discplina(materias)
