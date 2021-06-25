from django.test import TestCase

from catalog.models import Author


class AutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Execute uma vez para configurar dados não modificados para todos
        # os métodos de classe.
        """Cria-se um objeto autor que iremos usar mas não modificaremos
        em nenhum dos testes. Servirá para todos os teste"""
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Nome')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Falecimento')
