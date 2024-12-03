from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ProdutoModelForm
from produtos.models import Produto


class ProdutosView(PermissionRequiredMixin, ListView):
    permission_required = 'produtos.view_produtos'
    permission_denied_message = 'Vizualizar produto'
    model = Produto
    template_name = 'produtos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem produtos cadastrados!')


class ProdutoAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'produtos.add_produto'
    permission_denied_message = 'Cadastrar produto'
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto cadastrado com sucesso!'

class ProdutoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'produtos.update_produto'
    permission_denied_message = 'Editar produto'
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto atualizado com sucesso!'

class ProdutoDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'produtos.delete_produto'
    permission_denied_message = 'Eliminar produto'
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto deletado com sucesso!'