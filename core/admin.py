from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioChangeForm, CadastroModelAluno, CustomUsuarioForm
from .models import Professor, CustomUsuario, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'usuario_id')


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display =('first_name', 'last_name', 'email', 'matricula')
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Informações pessoais', {'fields': ('first_name', 'last_name', 'matricula')}),
            ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
        )


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula','nome','sexo', 'dataNasc', 'localNasc', 'nomeMae', 'nomePai', 'tel', 'cep', 'logr', 'uf', 'numero', 'bairro', 'cidade', 'complemento', 'turma', 'turno', 'ano', 'usuario')

admin.site.register(Aluno, AlunoAdmin)