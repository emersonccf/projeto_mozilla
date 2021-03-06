from catalog.forms import datetime, forms, ValidationError, _

""" import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _ """


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Informe uma data entre agora e 28 dias (padão 21 dias).",
        label="Nova data de devolução do livro",
    )

    """Uma das formas de validar um campo no formulário através do metodo
    clean_nome_do_campo_do_form_que_se_deseja_validar(self). Neste metodo do
    formulário será definidas as condições para que o campo seja considerado
    válido ou não
    """

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        # Verifica se a data informada está no passado
        if data < datetime.date.today():
            raise ValidationError(
                _('Data inválida - Data de devolução está no passado'))
        # Verifica se a data informada está acima de 28 dias de prazo
        if data > datetime.date.today() + datetime.timedelta(days=28):
            raise ValidationError(
                _('Data inválida - Data informada com prazo maior que 28 dias'))

        # retornando os dados verificados
        return data
