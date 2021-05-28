from catalog.models import *


class Book(models.Model):
    """ Representa o modelo de um livro (mas não os exeplares(cópias) de um livro) """
    title = models.CharField(
        "Título",
        max_length=200,
    )
    author = models.ForeignKey(
        "Author", # como o modelo Author ainda não tinha sido criado no momento da implementação do livro ele é indicado como string
        verbose_name="Autor",
        on_delete=models.SET_NULL,
        null=True,
    )
    summary = models.TextField(
        "Resumo",
        max_length=1000,
        help_text="Informe um resumo descritivo sobre o livro",
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>' 
    )
    genre = models.ManyToManyField(
        Genre, # Aqui o model Genre já tinha sido criado, então foi colocado o nome do model de forma explicita
        verbose_name="Gênero",
        help_text="Selecione um gênero para o livro"
    )

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


    def __str__(self) -> str:
        """ String que representa um livro """
        return self.title
    
    def get_absolute_url(self):
        """ Retona uma url para acesso aos detalhes do registro de um livro específico """
        # book-datail deve ser um nome associado a uma uls criada associada a uma view e seu respectivo template
        return reverse("book-detail", args=[str(self.id)])
    