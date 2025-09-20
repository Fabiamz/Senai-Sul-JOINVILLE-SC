class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class Biblioteca():
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")

#🏄‍♂️ TESTE DO SISTEMA
livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 2001)
livro2 = Livro("Diario de um Banana 1", "Jeff Kinney", 2007)
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
#🏄‍♂️ ATIVIDADE COMPLETA.