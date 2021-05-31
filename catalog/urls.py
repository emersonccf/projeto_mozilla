from django.urls.conf import path


from .views.IndexView import my_view, MyView, Index


urlpatterns = [
    #path('', my_view, name='index'), # - view como função
    #path('', MyView.as_view(), name='index'), # - view como classe
    path('', Index.as_view(), name='index'), # - view como classe
]
