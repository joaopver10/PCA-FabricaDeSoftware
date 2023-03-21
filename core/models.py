from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

difculdade = (
    ('Fácil', 'Fácil'),
    ('Médio', 'Médio'),
    ('Difícil', 'Difícil')
)

class Quiz(models.Model):
    nome = models.CharField(max_length=120)
    topico =models.CharField(max_length=120)
    num_de_questoes = models.IntegerField()
    tempo = models.IntegerField(help_text="Duração do quiz em minutos")
    pts_necessarios = models.IntegerField(help_text="Pontuação necessária em %")
    dificuldade = models.CharField(max_length=8, choices=difculdade)

    def __str__(self):
        return f"{self.nome}-{self.topico}"

    def get_questions(self):
        return self.questoes_set.all()

class Questoes(models.Model):
    pergunta = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    criado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.pergunta}

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    texto = models.TextField()
    correto = models.BooleanField(default=False)
    questao = models.ForeignKey(Questoes, on_delete = models.CASCADE)
    criado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Questão: {self.questao.pergunta}, Resposta: {self.texto}, Correto: {self.correto}"

'''
class Resultado(models.Model):
    quiz = models.ForeignKey()
    usuario = models.ForeignKey()
    pontos = models.FloatField()
'''