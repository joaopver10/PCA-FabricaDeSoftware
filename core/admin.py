from django.contrib import admin
from .models import Professor, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','professor')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno' )

