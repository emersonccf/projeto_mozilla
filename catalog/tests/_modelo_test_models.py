""" from django.test import TestCase

# python3 manage.py test
# python3 manage.py test --verbosity 2 (indo 0 a 3 nível de detalhe) ou
# python3 manage.py test -v 2 (indo 0 a 3 nível de detalhe)
# Executando testes específicos:
# python3 manage.py test catalog.tests.test_models.YourTestClass.test_one_plus_one_equals_two


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Execute uma vez para configurar dados não modificados para todos os métodos de classe.")
        pass

    def setUp(self):
        print(
            "setUp: Execute uma vez para cada método de teste para configurar dados limpos.")
        pass

    def test_false_is_false(self):
        print("Method: testa se falso é falso.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: testa se falso é verdadeiro.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: teste um mais um é igual a dois.")
        self.assertEqual(1 + 1, 2)
 """
