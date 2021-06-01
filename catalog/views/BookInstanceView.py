from catalog.models import *
from django.views.generic import DetailView


from catalog.models import *

class BookDetailView(DetailView):
    models = Book

    def get_queryset(self):
        return Book.objects.all()
    