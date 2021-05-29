from django.contrib import admin


from catalog.models import *


#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'date_of_birth', 'date_of_death' ]

    #list_filter = ['first_name']