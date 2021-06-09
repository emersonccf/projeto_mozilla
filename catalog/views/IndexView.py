from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  # necessário para view como classe

from catalog.models import Book, BookInstance, Author, Genre


def my_view(request):
    return HttpResponse("<h1>LocalLibrary - Seja bem-vindo - resposta de uma \
         Função</h1>")


class MyView(View):
    """ View que retorna uma resposta a uma solicitação do tipo GET """
    # define o que fazer quando o metodo que vem na requisição é GET
    # fica mais organizado o codigo melhor que fazzer if's dentro das funções
    # quando o metodo que vier na requisição for um: POST, DELETE, PUT, ETC...

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>LocalLibrary - Seja bem-vindo - resposta de \
            uma Classe</h1>")


class Index(View):

    def get(self, request, *args, **kwargs):
        num_books = Book.objects.all().count()
        # o all(), se não declarado, já é está implicito
        num_instances = BookInstance.objects.count()
        # disponível (status = 'd' ou seja Django field_name__exact = 'd')
        num_instances_available = BookInstance.objects.filter(
            status__exact='d').count()
        # o all(), se não declarado, já é está implicito
        num_authors = Author.objects.count()
        num_genre = Genre.objects.count()
        num_title_django = Book.objects.filter(
            title__icontains='django').count()

        # numero de visitas a esta página coforme a variável de sessão
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genre': num_genre,
            'num_title_django': num_title_django,
            'num_visits': num_visits,
        }
        return render(request, 'index.html', context=context)
