# Generated by Django 5.1.2 on 2024-12-01 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0003_alter_agendamento_options_agendamento_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamento',
            options={'ordering': ['-horario'], 'permissions': (('fechar_agendamento', 'Permite fazer o fechamento de um agendamento'),), 'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos'},
        ),
    ]
