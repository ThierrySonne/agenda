from msilib.schema import Property

from django.db import models

from ordemservicos.models import OrdemServicos


class Agendamento(models.Model):
    horario = models.DateTimeField('Horário',help_text='Data e hora do atendimento')
    cliente = models.ForeignKey('clientes.Cliente', verbose_name='Cliente', help_text='Nome do cliente',
                                on_delete=models.PROTECT)
    funcionario = models.ForeignKey('funcionarios.Funcionario', verbose_name='Funcionário',
                                    help_text='Nome do funcionário', on_delete=models.PROTECT)
    servico = models.ManyToManyField('servicos.Servico', verbose_name='Serviço', through='ordemservicos.OrdemServicos')
    valor = models.DecimalField('Valor total', max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField('Status',max_length=1, help_text='Status do agendamento', default='A')

    @property
    def servicos(self):
        return OrdemServicos.objects.filter(agendamento=self)

    class Meta:
        permissions = (('fechar_agendamento', 'Permite fazer o fechamento de um agendamento'),)
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['-horario']


    def __str__(self):
        return f'Cliente: {self.cliente}'
