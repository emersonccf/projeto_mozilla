from django.views.generic import DetailView
# necessário para requisitar logim para acesso a uma determinada view do tipo
# função do sistema: @login_required
from django.contrib.auth.decorators import login_required
# necessário para requisitar logim para acesso a uma determinada view do tipo
# classe do sistema
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Book


class BookDetailView(LoginRequiredMixin, DetailView):
    # LoginRequiredMixin deve ser declarada em primeiro lugar, antes de todas
    models = Book

    def get_queryset(self):  # sem adicionar essa função o sistema não funciona
        return Book.objects.all().order_by('title')
