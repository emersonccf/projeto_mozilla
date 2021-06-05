from catalog.views.BookInstanceView import BookDetailView
from django.urls.conf import path, re_path


from catalog.views.IndexView import my_view, MyView, Index
from catalog.views.BookView import BookListView
from catalog.views.AuthorView import AuthorListView
from catalog.views.AuthorDtView import AuthorDetailView

# Desafio para Exp. Reg. # r'^book/(?P<ano>\d{4})/(?P<mes>\d{2})/(?P<dia>\d{2})$'

urlpatterns = [
    #path('', my_view, name='index'), # - view como função
    #path('', MyView.as_view(), name='index'), # - view como classe
    path('', Index.as_view(), name='index'), # - view como classe
    path('books/', BookListView.as_view(), name='books'), 
    # outra forma de representara a url abaixo utilizado a re_path() com expessão regular
    # re_path(r'^books/(?P<pk>\d+)$', BookListView.as_view(), name='book-detail'), 
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'), 
    path('autors/', AuthorListView.as_view(), name='author'), 
    path('autors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'), 
]
