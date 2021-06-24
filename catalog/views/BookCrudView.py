# desafio final etapa.09
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from catalog.models import Book


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.9
    )
