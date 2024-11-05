from django.db import models


class OrdemServicos(models.Model):
    SITUACAO_OPCOES = (
        ('A','Agendado'),
        ('R','Realizado'),
        ('C','Cancelado'),
    )
    agendamento = models.ForeignKey('agendamentos.Agendamento',verbose_name='Agendamento', on_delete=models.CASCADE,
                                    related_name='agendamento')
    servico = models.ForeignKey('servicos.Servico',verbose_name='Serviço',on_delete=models.CASCADE,
                                related_name='ordem_servico')
    funcionario = models.ForeignKey('funcionarios.Funcionario',verbose_name='Funcionário', on_delete=models.CASCADE,
                                    related_name='funcionario')
    situacao = models.CharField('Situação', max_length=1, choices=SITUACAO_OPCOES, default='A')
    observacoes = models.TextField('Observações', max_length=300, blank=True, null=True)
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, help_text='Preço do Serviço',
                                default=0.00)

    class Meta:
        verbose_name = 'Serviço realizado'
        verbose_name_plural = 'Serviços realizados'

        constraints = [models.UniqueConstraint(fields=['agendamento', 'servico'], name='constraint_agendamento')]

    def __str__(self):
        return self.servico.nome