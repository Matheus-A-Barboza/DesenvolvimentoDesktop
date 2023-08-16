class Livros():
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = 2023

    def novo_ano(self, upd_ano):
        self.ano = upd_ano


    def show_catolog(self):
        print(f'Titulo: {self.titulo}\n'
              f'Autor: {self.autor}\n'
              f'Genero: {self.genero}\n'
              f'Ano de Publicação: {self.ano}')

livro1 = Livros('A Cartomante','Machado de Assis','Ficcao')

livro1.novo_ano(1896)

print('------------------------|')
livro1.show_catolog()
print('------------------------|')