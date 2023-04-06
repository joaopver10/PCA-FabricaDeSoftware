from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
import datetime
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager):

    use_in_migrations = True

    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff= True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser= True.')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    """User model."""

    email = models.EmailField("E-mail", unique=True)
    matricula = models.CharField("Matrícula", max_length=7)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.email}, {self.matricula}"

    objects = UserManager() ## This is the new line in the User model. ##


class Aluno(models.Model):

    choices_sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    choices_turno = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20, choices=choices_sexo)
    dataNasc = models.DateField(default = datetime.datetime.now)
    localNasc = models.CharField(max_length=30)
    nomePai = models.CharField(max_length=30)
    nomeMae = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    cep = models.CharField(max_length=10)
    logr = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    complemento = models.CharField(max_length=30)
    turma = models.CharField(max_length=10)
    turno = models.CharField(max_length=20, choices=choices_turno)
    ano = models.CharField(max_length=4)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuário" ,on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.matricula},{self.sexo}, {self.dataNasc}, {self.localNasc}, {self.nomeMae}, {self.nomePai}, {self.tel}, {self.cep}, {self.logr}, {self.uf}, {self.numero}, {self.bairro}, {self.cidade},{self.complemento}, {self.turma}, {self.turno}, {self.ano}, {self.usuario}"

class Professor(models.Model):
    email = models.EmailField("E-mail")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuário", on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Quiz(models.Model):
    difculdade = (
        ('Fácil', 'Fácil'),
        ('Médio', 'Médio'),
        ('Difícil', 'Difícil')
    )
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