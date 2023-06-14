from ast import Return
from django.db import models
from django.core.exceptions import ValidationError

PROFESSORES = [
    ('Nilton Cesar Sacco', 'Nilton Cesar Sacco'),
    ('Orlando Saraiva Júnior','Orlando Saraiva Júnior'),
    ('Thiago Mendes','Thiago Mendes'),
    ('Sama Rouani','Sama Rouani'),
]

DISCIPLINA = [
    ('Banco de Dados Relacional', 'Banco de Dados Relacional'),
    ('Desenvolvimento Web III', 'Desenvolvimento Web III'),
    ('Banco de Dados Não Relacional', 'Banco de Dados Não Relacional'),
    ('Técnicas de Programação II', 'Técnicas de Programação II'),

]


def validate_min_length(value):
    if len(value) < 10:
        raise ValidationError('O campo deve ter no mínimo 10 caracteres.')


class ListaModels(models.Model):
    
    aluno = models.CharField('aluno', max_length=200,
                             validators=[validate_min_length])
    professor = models.CharField(
        'professor', max_length=200, choices=PROFESSORES)
    

    
    def __str__(self):
        return "{} ({})".format(self.aluno, self.professor)
