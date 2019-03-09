class Evento:
    def __init__(self,nome,data,local):
        self.nome = nome
        self.data = data
        self.local = local
class Pessoa:
    def __init__(self,nome):
        self.nome = nome
class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf):
        super().__init__(nome)
        self.cpf = cpf
class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
class Autor(Pessoa):n
    def __init__(self,nome, artigos):
        super.__init__(nome)
        self.artigos = artigos
class Artigos:
    def __init__(self,titulo, palavra_chave ,data):
        self.titulo = titulo
        self.palavra_chave = palavra_chave
        self.data = data
class AutorArtigo:
    def __init__(self,autor,artigo):
        pass