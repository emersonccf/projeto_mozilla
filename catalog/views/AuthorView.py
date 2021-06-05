from django.views.generic import ListView

from catalog.models import *


class AuthorListView(ListView):
    model = Author
    paginate_by = 2

    def get_queryset(self):
        return Author.objects.all()
    

