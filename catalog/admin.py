from django.contrib import admin
from catalog.models.author import Author
from catalog.models.genre import Genre
from catalog.models.book import Book
from catalog.models.bookinstance import BookInstance


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)