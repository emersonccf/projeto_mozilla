from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from catalog.models import BookInstance


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    models = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user) \
            .filter(status__exact='e').order_by('due_back')
