from django.urls import path

from .views import cadastro, aluno

urlpatterns=[
    path('', cadastro, name='cadastro'),
    path('aluno/', aluno, name='aluno')
]