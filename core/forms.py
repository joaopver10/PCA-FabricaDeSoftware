from django import forms as fm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario, Aluno


class CustomUsuarioForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name', 'matricula']
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name', 'matricula']


