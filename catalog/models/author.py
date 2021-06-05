from catalog.models import *

class Author(models.Model):
    """ Model que representa um autor """
    first_name = models.CharField(
        "Nome",
        max_length=100,
    )
    last_name = models.CharField(
        "Sobrenome",
        max_length=100,
    )
    date_of_birth = models.DateField(
        "Data de Nascimento",
        null=True,
        blank=True,
    )
    date_of_death = models.DateField(
        'Falecimento',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        """ String que representa um autor """
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        """ Retorna o url para acessar uma instância particular do autor """
        return reverse("author-detail", kwargs={"pk": self.pk})
