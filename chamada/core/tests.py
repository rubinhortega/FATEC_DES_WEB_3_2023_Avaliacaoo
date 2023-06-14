from django.test import TestCase
from .models import ListaModels

class ChamadaTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200(self):
        self.assertEqual(200, self.resp.status_code)

    def test_Texto(self):
        self.assertContains(self.resp, 'Aluno')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'Chamada.html')

class ChamadaModelTest(TestCase):
    def setUp(self):
        self.chamada = ListaModels(
            aluno='Aluno de teste',
            professor='Nilton Cesar Sacco - Banco de Dados Relacional',
        )
        self.chamada.save()

    def test_criado(self):
        self.assertTrue(ListaModels.objects.exists())

    def test_criado_somente_um(self):
        self.assertTrue(len(ListaModels.objects.all()) == 1)
