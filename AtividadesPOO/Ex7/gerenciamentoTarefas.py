class Tarefas():
    def __init__(self, desc, dtCria):
        self.desc = desc
        self.dtCria = dtCria
        self.concluida = False

    def tarefa_concluida(self):
        self.concluida = True

    def exibir_detalhes(self):
        status = 'Concluida' if self.concluida else 'Não Concluida'
        detalhes = f'Descrição: {self.desc}\nData de Criação: {self.dtCria}\nStatus: {status}'
        print(detalhes)

tarefa1 = Tarefas('Trabalhar','16/08/2023')
tarefa2 = Tarefas('Faculdade','16/08/2023')

tarefa1.tarefa_concluida()
tarefa1.exibir_detalhes()
print()
tarefa2.exibir_detalhes()