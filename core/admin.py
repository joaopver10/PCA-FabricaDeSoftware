from django.contrib import admin
from .models import Questoes, Justificativas, RespostasCorreta, RespostasIncorretas

@admin.register(Justificativas)
class JustificativasAdmin(admin.ModelAdmin):
    list_display = ("id", "justificativa")

@admin.register(RespostasCorreta)
class RespostasCorretaAdmin(admin.ModelAdmin):
    list_display = ("id", "resposta")

@admin.register(RespostasIncorretas)
class RespostasIncorretasAdmin(admin.ModelAdmin):
    list_display = ("id", "respostaa", "respostab", "respostac")

@admin.register(Questoes)
class QuestoesAdmin(admin.ModelAdmin):
    list_display = ("id", "pergunta", "materia", "dificuldade", "respostacorreta", "respostaincorreta", "justifica")

