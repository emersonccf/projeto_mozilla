from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # necessário para view como classe

from catalog.models import *

def my_view(request):
    return HttpResponse("<h1>LocalLibrary - Seja bem-vindo - resposta de uma Função</h1>")

class MyView(View):
    """ View que retorna uma resposta a uma solicitação do tipo GET """
    # define o que fazer quando o metodo que vem na requisição é GET
    # fica mais organizado o codigo melhor que fazzer if's dentro das funções quando 
    # quando o metodo que vier na requisição for um: POST, DELETE, PUT, ETC... 
    def get(self, request, *args, **kwargs): 
        return HttpResponse("<h1>LocalLibrary - Seja bem-vindo - resposta de uma Classe</h1>")

class Index(View):

    def get(self, request, *args, **kwargs):
        num_books = Book.objects.all().count() 
        num_instances = BookInstance.objects.count() # o all(), se não declarado, já é está implicito
        # disponível (status = 'd' ou seja Django field_name__exact = 'd')
        num_instances_available = BookInstance.objects.filter(status__exact='d').count()
        num_authors = Author.objects.count() # o all(), se não declarado, já é está implicito
        num_genre = Genre.objects.count()
        num_title_django = Book.objects.filter(title__icontains='django').count()

        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genre': num_genre,
            'num_title_django': num_title_django,
        }
        return render(request, 'index.html', context=context)