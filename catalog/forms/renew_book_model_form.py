from catalog.forms import ModelForm, _, ValidationError, datetime
from catalog.models import BookInstance  # etapa 9 v2 do form


class RenewBookModelForm(ModelForm):

    """Uma das formas de validar um campo no formulário através do metodo
    clean_nome_do_campo_do_form_que_se_deseja_validar(self). Neste metodo do
    formulário será definidas as condições para que o campo seja considerado
    válido ou não
    """
    # só precisamos ajustar aqui o nome do campo que no model se chama due_back
    # que no fomulario criado anteriomente se chamava renewal_date

    def clean_due_back(self):
        data = self.cleaned_data['due_back']
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

    # Na classse meta do formulário podemos altera algumas definições
    # realizadas no model como por exemplo o rótulo do campo, o texto de ajuda,
    # o widget, a mensagem de erro, etc.

    class Meta:
        # nome do model que se deseja criar o formulario
        model = BookInstance
        # lista de campos que serão incluidos no formulário, quessessemos todos
        # colocaria-se fields = '__all__' ou caso necessitassemos excluir algum
        # utilizaria-se exclude = ['campos_que_se_deseja_nao_exibir', ...]
        # O restante das informações vem das definições de campo do modelo
        # (ex. rótulos, widgets, texdo de ajuda, mensagens de erro)
        fields = ['due_back', ]
        # redefine títulos dos campos
        labels = {
            'due_back': _('Nova data de devolução do livro'),
        }
        # redefine texto de ajuda dos campos
        help_texts = {
            'due_back': _('Informe uma data entre agora e 28'
                          'dias (padão 21 dias).'),
        }
