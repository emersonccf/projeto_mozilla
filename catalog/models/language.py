from catalog.models import *

class Language(models.Model):
    """ Representa idioma / língua do livro cadastrado  """
    
    name = models.CharField(
        'Nome',
        max_length=200,
        help_text='Informe um nome de idioma (ex. Francês)',
    )

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self) -> str:
        return self.name