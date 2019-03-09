"""
    Usar letras MAIUSCULAS na primeira letra de class (sujeito a perda de pontos)

"""
class Projeto:
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    def __str__(self):
        return 'Projeto: ' + self.nome + ', '+ self.data_inicio + self.data_fim
class Pessoa:
    #posso definir atributos direto na class!
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.status = "Ativo"
    def finalizar(self):
        self.status = 'Finalizado'
    def __str__(self):
        return "Pessoa: " + self.nome+ self.data_nascimento
class Atividade:
    def __init__(self,nome,prioridade,pessoa,projeto,data_inicio,data_fim):
        self.nome= nome
        self.prioridade = prioridade
        self.pessoa = pessoa
        self.projeto = projeto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    def __str__(self):
        return "Atividade: " + self.nome + self.pessoa #+ self.projeto + self.data_inicio +self.data_fim
class ProjetoAtividade:
    def __init__(self,atividade, projeto):
        self.atividade = atividade
        self.projeto = projeto
p = Projeto('Projct','15/02/2019','22/02/2019')
pes = Pessoa('Cleiton', '20/02/2000')
at = Atividade('Nive', 5, pes,p,'20/02/2019','21/02/2019')
pa = ProjetoAtividade(at, p)
print(pa)
