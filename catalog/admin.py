from django.contrib import admin


from catalog.models import *


admin.site.register(Genre)
admin.site.register(Language)

class BookInLine(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #define os campos que irão apararecer na display lista e como irão ser mostrados
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    #define os campos que serão exibidos nos formulários de adição e modificação e 
    # se na vertical ou na horizontal (nesse caso os campos devem estar agrupados em
    # uma tupla como elemento da lista como o exemplo abaixo para as datas)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInLine]

class BooksIntanceInLine(admin.TabularInline):
    # define uma classe para representar as instâncias em formato tabular, em linha
    # para ser incluida na apresntação do formulario dos livros
    model = BookInstance
    extra = 0 # linhas adcionais para inserir novo exemplar, por padão aparecem 3, melhor deixar como 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):                  #display_genre-> função definida no model
    list_display = ['title', 'author', 'language', 'display_genre']
    inlines = [BooksIntanceInLine] # formularios de exemplares em linha dentro de livros

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book','status', 'due_back', 'id']
    list_filter = ['status', 'due_back']
    # agrupa os campos por seção conforme a estrutura da tupla abaixo 
    fieldsets = (
        (
            'Dados do Exemplar', {
                'fields': ('book', 'imprint', 'id')
            }
        ),
        (
            'Disponibilidade', {
                'fields': ('status', 'due_back')
            }
        ),
    )