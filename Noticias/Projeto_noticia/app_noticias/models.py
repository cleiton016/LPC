from django.db import models
class Noticia(models.Model):
    conteudo = models.TextField()
    titulo = models.CharField('título', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField('Data da Criação')
    data_publicacao = models.DateTimeField('Data da publicação')
    publicado = models.BooleanField('Publicado')
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    def __str__(self):
        return self.titulo
# Create your models here.
