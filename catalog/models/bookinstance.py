from catalog.models import models, uuid, LOAN_STATUS, Book, User
from datetime import date


class BookInstance(models.Model):
    """ Representa um exemplar específico de um livro que pode ser emprestado
    na biblioteca """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='ID exclusivo para o livro específico em toda a biblioteca',
    )
    book = models.ForeignKey(
        Book,
        verbose_name="Livro",
        on_delete=models.SET_NULL,
        null=True,
    )
    imprint = models.CharField(
        'Detalhes da Edição',
        max_length=200,
    )
    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Mutuário',
        help_text='Usuário que pegou o livro emprestado'
    )
    due_back = models.DateField(
        'Data de Devolução',
        null=True,
        blank=True,
    )
    status = models.CharField(
        'Situação do exemplar',
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Disponibilidade do exemplar',
    )

    class Meta:
        ordering = ['due_back']
        verbose_name = "Exemplar"
        verbose_name_plural = "Exemplares"

    def __str__(self):
        """ String que representa um exemplar do livro """
        return f"{self.id} - ({self.book.title})"

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
