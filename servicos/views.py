from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator

from servicos.forms import ServicoModelForm
from servicos.models import Servico


class ServicosView(ListView):
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset()

        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar)|Q(nome__icontains=buscar))

        if qs.count()>0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem servicos cadastrados!')


class ServicoAddView(SuccessMessageMixin, CreateView):
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço cadastrado com sucesso!'

class ServicoUpdateView(SuccessMessageMixin, UpdateView):
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço atualizado com sucesso!'

class ServicoDeleteView(SuccessMessageMixin, DeleteView):
    model = Servico
    template_name = 'servico_apagar.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço deletado com sucesso!'
