from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
SEXOS = [
    ('feminino', 'Feminino'),
    ('masculino', 'Masculino'),
    ('outro', 'Outro')
]

PRESIDENTES = [
    ('Jair Bolsonaro', 'Jair Bolsonaro'),
    ('Luiz Inacio Lula da Silva', 'Luiz Inacio Lula Da Silva'),
    ('Marina Silva', 'Marina Silva'),
    ('Ciro Gomes', 'Ciro Gomes'),
    ('nulo', 'Nulo'),
    ('branco', 'Branco'),
]


def age_validate(value):
    if value < 16:
        raise ValidationError(('Menores de 16 não podem votar. Idade inserida:  %(value)'), params={'value': value}, )


class Vote(models.Model):
    cpf = models.CharField(max_length=250, unique=True)
    sexo = models.CharField(max_length=250, choices=SEXOS, null=False)
    idade = models.PositiveIntegerField(default=16, null=False)
    presidente = models.CharField(max_length=250, choices=PRESIDENTES, null=False)
    audio = models.TextField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
