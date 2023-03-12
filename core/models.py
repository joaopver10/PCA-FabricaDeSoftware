from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

dificuldade = (
    ('f','Facil'),
    ('m','Medio'),
    ('d','Dificil'),
)

class Justificativas(models.Model):
    justificativa = models.TextField('Justificativa')

    def __str__(self):
       return self.justificativa

class RespostasCorreta(models.Model):
    resposta = models.CharField('Resposta', max_length=250)

    def __str__(self):
       return self.resposta

class RespostasIncorretas(models.Model):
    respostaa = models.CharField('Resposta 1', max_length=250)
    respostab = models.CharField('Resposta 2', max_length=250)
    respostac = models.CharField('Resposta 3', max_length=250)

    def __str__(self):
        return f'{self.respostaa} ' \
              f'{self.respostab}' \
              f'{self.respostac}'



class Questoes(models.Model):
    pergunta = models.TextField('Pergunta')
    materia = models.CharField('Materia', max_length=100)
    dificuldade = models.CharField('Dificuldade', max_length=10,choices=dificuldade)
    respostacorreta = models.ForeignKey(RespostasCorreta, on_delete=models.CASCADE)
    respostaincorreta = models.ForeignKey(RespostasIncorretas, on_delete=models.CASCADE)
    justifica = models.ForeignKey(Justificativas, on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.pergunta} ' \
              f'{self.materia} ' \
              f'{self.dificuldade}' \



