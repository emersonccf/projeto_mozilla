from catalog.models import *
from django.views.generic import DetailView


from catalog.models import *

class BookDetailView(DetailView):
    models = Book

    def get_queryset(self): # sem adicionar essa função o sistema não funcionou
        return Book.objects.all().order_by('title') 
    