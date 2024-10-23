from django import forms

from .models import Funcionario

class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'fone', 'email', 'foto', 'data_admissao']

        error_messages = {
            'nome': {'required': 'O nome do funcionario é um campo obrigatório'},
            'fone': {'required': 'O número do funcionario é um campo obrigatório'},
            'email': {'required': 'O e-mail do funcionario é um campo obrigatório',
                      'invalid': 'Formato inválido para o e-mail. Exemplo de formato válido: fulano@dominio.com',
                      'unique': 'E-mail já cadastrado'
            },
            'data_admissao': {'required': 'A data de admissão é um campo obrigatório'},
        }