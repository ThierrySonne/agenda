# Generated by Django 5.1.2 on 2024-11-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0002_agendamento_servico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamento',
            options={'ordering': ['-horario'], 'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos'},
        ),
        migrations.AddField(
            model_name='agendamento',
            name='status',
            field=models.CharField(default='A', help_text='Status do agendamento', max_length=1, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Valor total'),
        ),
    ]