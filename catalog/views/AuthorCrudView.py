# necessário para criar as views genéricas que irão herdar destas classes
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from catalog.models import Author


# etapa 9 desafio PermissionRequiredMixin
class AuthorCreate(PermissionRequiredMixin, CreateView):
    # para criar:
    # necessário definir o model que será a base
    model = Author
    # a relação de campos que iremos utilizar na criação, nesse caso todos
    fields = '__all__'
    # os valores iniciais que se deseja para campos específicos
    initial = {
        'date_of_death': '05/01/2018',  # para demostração, pode remover depois
    }
    # por padrão, estas será redirecionado para a ListView de autores que
    # foi criada em tutorial anterior. Pode ser definido um caminho, url
    # alternativa success_url = 'caminho_alternativo' como realizado
    # AuhorDelete
    # o nome do template para criação e alteração recebem o mesmo nome padrão
    # é nome-do-model_form.html que pode ser alterado. Uma das formas de
    # o nome, por exemplo é modificando o sufixo através do atributo
    # template_name_suffix = '_crud' onde pode ser definido outro sufixo no
    # lugar do sufixo _form.
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )

# etapa 9 desafio PermissionRequiredMixin


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    # relação de campos que serão listados
    fields = [
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
    ]
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )
# etapa 9 desafio PermissionRequiredMixin


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    # para excluir não precisa exibir nenhum campo por isso não temos fields
    model = Author
    # caminho alternativo para onde será redirecionado em caso de sucesso, pois
    # para exlusão Django não define um valor padrão para esse caminho.
    # a função reverse_lazy('nome_de_uma_url') é uma versão preguiçosa de
    # reverse(), usado pq estamos utilizando para definir um atributo desta
    # classe
    success_url = reverse_lazy('author')
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )
