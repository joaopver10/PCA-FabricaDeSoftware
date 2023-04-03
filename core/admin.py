from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm
from .models import Professor, Aluno, Users

"""@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','professor')
"""

"""
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_nascimento')
"""


@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Sexo', {'fields': ('sexo',)}),
        ('Data Nascimento', {'fields': ('dataNasc',)}),
        ('localNasc', {'fields': ('localNasc',)}),
        ('nomePai', {'fields': ('nomePai',)}),
        ('nomeMae', {'fields': ('nomeMae',)}),
        ('tel', {'fields': ('tel',)}),
        ('cep', {'fields': ('cep',)}),
        ('logr', {'fields': ('logr',)}),
        ('numero', {'fields': ('numero',)}),
        ('bairro', {'fields': ('bairro',)}),
        ('cidade', {'fields': ('cidade',)}),
        ('complemento', {'fields': ('complemento',)}),
        ('turma', {'fields': ('turma',)}),
        ('turno', {'fields': ('turno',)}),
        ('ano', {'fields': ('ano',)}),
    )
