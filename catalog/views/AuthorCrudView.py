from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Author


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {
        'date_of_death': '05/01/2018',
    }


class AutorUpdate(UpdateView):
    model = Author
    fields = [
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
    ]


class AutorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
