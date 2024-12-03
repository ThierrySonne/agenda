from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.context_processors import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import FornecedorModelForm
from .models import Fornecedor

class FornecedoresView(PermissionRequiredMixin, ListView):
    permission_required = 'fornecedores.view_fornecedor'
    permission_denied_message = 'Vizualizar fornecedor'
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem fornecedores cadastrados!')

class FornecedorAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'fornecedores.add_fornecedor'
    permission_denied_message = 'Cadastrar fornecedor'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor cadastrado com sucesso!'

class FornecedorUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'fornecedores.change_fornecedor'
    permission_denied_message = 'Editar fornecedor'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor atualizado com sucesso!'

class FornecedorDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'fornecedores.delete_fornecedor'
    permission_denied_message = 'Eliminar fornecedor'
    model = Fornecedor
    template_name = 'fornecedor_apagar.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor apagado com sucesso!'