from django.urls import path

from .views import cadastro, quiz

urlpatterns=[
    path('', cadastro, name='cadastro'),
    path('quiz/', quiz, name='quiz')
]