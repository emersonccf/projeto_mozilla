from django.urls.conf import path


from .views import my_view


urlpatterns = [
    path('', my_view)
]
