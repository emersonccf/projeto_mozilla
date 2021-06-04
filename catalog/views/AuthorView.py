from django.views.generic import ListView

from models import *


class AuthorListView(ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()
    

