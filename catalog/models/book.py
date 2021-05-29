from catalog.models import *


class Book(models.Model):
    """ Representa o modelo de um livro (mas não os exeplares(cópias) de um livro) """
    title = models.CharField(
        "Título",
        max_length=200,
    )
    # a relação estabelecida foi: Autor 0..1  <--->  0..* Livros
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
    # a relação estabelecida foi: Genero 0..*  <--->  0..* Livros
    genre = models.ManyToManyField(
        Genre, # Aqui o model Genre já tinha sido criado, então foi colocado o nome do model de forma explicita
        verbose_name="Gênero",
        help_text="Selecione um gênero para o livro"
    )
    # a relação estabelecida foi: Idioma 0..1  <--->  0..* Livros
    language = models.ForeignKey(
        'Language',
        on_delete=models.SET_NULL,
        null= True,
        verbose_name='Idioma',
        help_text='Informe o idioma em que foi escrito o livro',
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
    
    def display_genre(self):
        """ Cria uma string para Gênero - Isto é requerido no display da classe BookAdmin em admin.py
        (muitos-para-muitos) 
        não é recomendado pelo custo computacional de acesso ao BD só para 
        exemplificar que é possível """
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    # nome que irá aparece como titulo da coluna no admin, se omitido aparece o nome da função como título
    display_genre.short_description = "Gênero" 
    