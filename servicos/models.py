from django.db import models
from django.db.models.functions import Upper

from produtos.models import Produto
from produtosservico.models import ProdutosServico


# Create your models here.
class Servico(models.Model):
    nome = models.CharField('nome',max_length=100,help_text='Nome completo do servico', unique=True)
    preco = models.CharField('preco',max_length=5, help_text='Preço do servico')
    descricao = models.TextField('descricao', max_length=300, help_text='Descricao e observacoes do servico')
    produto = models.ManyToManyField('produtos.Produto', through='produtosservico.ProdutosServico')


    @property
    def produtos(self):
        return ProdutosServico.objects.filter(servico=self)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural ='Serviços'
        ordering = [Upper('nome')]

    def __str__(self):
        return self.nome
