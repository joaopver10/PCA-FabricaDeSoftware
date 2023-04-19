from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioChangeForm, CustomUsuarioForm
from .models import Professor, CustomUsuario, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'usuario_id')


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display =('id','first_name', 'last_name', 'email','is_student', 'is_teacher')
    fieldsets = (
            (None, {'fields': ('email', 'password','is_student' , 'is_teacher')}),
            ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
            ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
        )


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula','nome','sexo', 'dataNasc', 'localNasc', 'nomeResponsavel', 'tel', 'cep', 'logr', 'uf', 'numero', 'bairro', 'cidade', 'complemento', 'turma', 'turno', 'ano', 'professor_id', 'usuario_id')

admin.site.register(Aluno, AlunoAdmin)