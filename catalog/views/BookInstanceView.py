from catalog.models.bookinstance import BookInstance
from django.views.generic import DetailView
# necessário para requisitar logim para acesso a uma determinada view do tipo
# função do sistema: @login_required
# from django.contrib.auth.decorators import login_required
# necessário para requisitar logim para acesso a uma determinada view do tipo
# classe do sistema
from django.contrib.auth.mixins import LoginRequiredMixin
# etapa 9 - formulario de renovação de livros
import datetime  # etapa - 9

from django.shortcuts import render, get_object_or_404  # etapa - 9
from django.http import HttpResponseRedirect  # etapa - 9
from django.urls import reverse  # etapa - 9
from django.contrib.auth.decorators import permission_required  # etapa - 9

from catalog.models import Book
# etapa 9 - formulario de renovação de livros
from catalog.forms import RenewBookForm  # etapa - 9


class BookDetailView(LoginRequiredMixin, DetailView):
    # LoginRequiredMixin deve ser declarada em primeiro lugar, antes de todas
    models = Book

    def get_queryset(self):  # sem adicionar essa função o sistema não funciona
        return Book.objects.all().order_by('title')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    # instancia um exemplar de livro baseado na chave primária, caso não ache
    # devolve mosta uma pagina com o erro 404 (não encontrada)
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # Se o método http for POST então processa os dados do formulario
    if request.method == 'POST':
        # Cria uma instancia do formulário e povoa com os dados da requisição
        # realiza um binding aqui
        form = RenewBookForm(request.POST)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Processa os dados em form.cleaned_data (dados limpos)
            # como estamos renovando a data de devolução do livro só
            # necessitamos alterar reescrever o campo due_back
            book_instance.due_back = form.cleaned_data['renewal_date']
            """Importante: Embora você também possa acessar os dados do
            formulário diretamente por meio do request (por exemplo,
            request.POST['renewal_date'] ou request.GET['renewal_date']
            se utilizando requisição GET), isso NÃO é recomendado.
            O dado limpo é "higienizado", validado, e convertido em tipo
            compatível com Python."""
            book_instance.save()
            # redirecina para uma nova URL (todos os emprestimos)
            return HttpResponseRedirect(reverse('all-borrowed'))
        # se o metodo de requisicao for GET ou outro qualquer então cria um
        # formulário padrão
    else:
        #  cria uma proposta de data de revalidação com intervalo de 21dias
        propoused_renewal_date = datetime.date.today() + \
            datetime.timedelta(days=21)
        # cria um formulario que recebe dados iniciais, no caso a posposta
        # de data de renovalçao do livro
        form = RenewBookForm(initial={
            'renewal_date': propoused_renewal_date,
        })
    # cria o dicionario de contexto passando o formulario e a instacia
    # do livro que se deseja renovar
    context = {
        'form': form,
        'book_instance': book_instance,
    }
    # retorna renderização de um html, passando nessa ordem:
    # a requisição, a string do caminho e nome do html e a
    # dicionario de contexto contendo as informações para renderizar
    # corretamente o html
    return render(request, 'catalog/book_renew_librarian.html',
                  context)
