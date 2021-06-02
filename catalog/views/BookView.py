from django.views.generic import ListView 


from catalog.models import *

class BookListView(ListView):
    model = Book # informa a que model a view está vinculada
    paginate_by = 2 #informa a quantidade e livros por página na listagem do site
    
    # custumização abaixo é opicional dentro da necessidade de cada view
    """ context_object_name = 'my_book_list' # seu próprio nome para a lista como uma variável de modelo 
    queryset = Book.objects.filter(title__icontains='django')[:1] # Obtenha o primeiro livro contendo no título a palavra 'django' 
    template_name = 'books/my_arbitrary_template_name_list.html' # Especifique seu próprio nome/localização do template """

    def get_queryset(self):
        # Obtenha o primeiro livro contendo no título a palavra 'django' 
        return Book.objects.all()#filter(title__icontains='django').order_by('title')[:2] 
    
    # se quisermos adicionar algum outro dado na variável de contexto book_list
    # sobreescrevemos o metodo abaixo da seguinte forma: importante seguir o padrão abaixo
    def get_context_data(self, **kwargs):
        # Chame a implementação de base primeiro para obter o contexto
        context = super(BookListView, self).get_context_data(**kwargs)
        # Crie quaisquer dados e adicione-os ao contexto 
        context['text'] = "Meu pequeno texto passado no contexto do dicionário"
        return context
        