from catalog.models import *


class Genre(models.Model):
    """ Modelo que representa um genero de um livro """
    name = models.CharField(
        "Nome",
        max_length=200,
        help_text="Informe o genero do livro do livro (ex. Ficção Científica)",
    )

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self) -> str:
        """ String para representar um gênero """
        return self.name