from django.views.generic import DetailView

from catalog.models import *

class AuthorDetailView(DetailView):
    models = Author

    def get_queryset(self):
        return Author.objects.all()
    