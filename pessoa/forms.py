from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Pessoa
        fields = ['nome_completo','data_nascimento','ativa']
        #poderia ser fields = ['__all__'] dessa forma viria todos
