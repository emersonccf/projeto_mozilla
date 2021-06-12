from django.contrib.auth.mixins import PermissionRequiredMixin  # desafio et.8
# from django.contrib.auth.decorators import permission_required  # desafio et.8
from django.views.generic import ListView

from catalog.models.bookinstance import BookInstance


class AllBorrowedBooksView(PermissionRequiredMixin, ListView):
    models = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all_user.html'
    permission_required = (
        'catalog.can_mark_returned',  # desafio et.8
    )
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='e') \
            .order_by('due_back')
