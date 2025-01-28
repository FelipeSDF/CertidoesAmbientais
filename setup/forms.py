from .models import  Report, Certificate, Report_fisico
from django import forms




class ReportForm(forms.ModelForm):
    class Meta():
        model = Report
        fields = '__all__'
        # exclude = ['photos', 'Reports']
        
        pavimentation_choices = (['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        eletricity_choices =(['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        ilumination_choices =(['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        quantity_houses_choices =(['muitas','muitas'],['algumas','algumas'],['poucas','poucas'],['nenhuma','nenhuma'])
        
        
        widgets = {
            'number': forms.NumberInput(attrs=({'class': 'form-input', 'image':'alksjdlkajsdkjlas'})),
            'data':  forms.TextInput(attrs=({'type':'date','class': 'form-input'})),
            'datetime_created':  forms.TextInput(attrs=({'class': 'form-input'})),
            'local':  forms.TextInput(attrs=({'class': 'form-input'})),
            'bairro':  forms.TextInput(attrs=({'class': 'form-input'})),
            'unidade':  forms.TextInput(attrs=({'class': 'form-input'})),
            'obs':  forms.TextInput(attrs=({'class': 'form-input'})),
            'pavimentation':  forms.Select(choices=pavimentation_choices, attrs=({'class': 'form-input'})),
            'eletricity':  forms.Select(choices=eletricity_choices, attrs=({'class': 'form-input'})),
            'ilumination':  forms.Select(choices=ilumination_choices, attrs=({'class': 'form-input'})),
            'quantity_houses':  forms.Select(choices=quantity_houses_choices, attrs=({'class': 'form-input'})),
        }
        
        icons = {
            'number':'https://img.icons8.com/?size=48&id=2YHBrgJkUHzJ&format=png',
            'data':'https://img.icons8.com/?size=30&id=ilO1-m5bKBS4&format=png',
            'datetime_created':'https://img.icons8.com/?size=40&id=61987&format=png',
            'local':'https://img.icons8.com/?size=40&id=61987&format=png',
            'bairro':'https://img.icons8.com/?size=48&id=81284&format=png',
            'unidade':'https://img.icons8.com/?size=48&id=80414&format=png',
            'obs':'https://img.icons8.com/?size=48&id=7VIEQ1GiK0Iz&format=png',
            'pavimentation':'https://img.icons8.com/?size=48&id=MEwb2lHaMFxX&format=png',
            'eletricity':'https://img.icons8.com/?size=48&id=xLj25NrPMxFQ&format=png',
            'ilumination':'https://img.icons8.com/?size=48&id=wFfu6zXx15Yk&format=png',
            'quantity_houses':'https://img.icons8.com/?size=64&id=118996&format=png',
            'Reports':'https://img.icons8.com/?size=48&id=11849&format=png',
}

class ReportFisicoForm(forms.ModelForm):
    class Meta():
        model = Report_fisico
        fields = '__all__'
        # exclude = ['photos', 'Reports']
        
        pavimentation_choices = (['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        eletricity_choices =(['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        ilumination_choices =(['presente','presente'],['parcialmente presente','parcialmente presente',],['ausente','ausente'])
        
        quantity_houses_choices =(['muitas','muitas'],['algumas','algumas'],['poucas','poucas'],['nenhuma','nenhuma'])
        
        
        widgets = {
            'requerente': forms.TextInput(attrs=({'class': 'form-input'})),
            'latitude': forms.NumberInput(attrs=({'class': 'form-input'})),
            'longitude': forms.NumberInput(attrs=({'class': 'form-input'})),
            'cpf_cnpj': forms.NumberInput(attrs=({'class': 'form-input'})),
            'code': forms.NumberInput(attrs=({'class': 'form-input'})),
            'number': forms.NumberInput(attrs=({'class': 'form-input'})),
            'data':  forms.TextInput(attrs=({'type':'date','class': 'form-input'})),
            'datetime_created':  forms.TextInput(attrs=({'class': 'form-input'})),
            'local':  forms.TextInput(attrs=({'class': 'form-input'})),
            'bairro':  forms.TextInput(attrs=({'class': 'form-input'})),
            'unidade':  forms.TextInput(attrs=({'class': 'form-input'})),
            'obs':  forms.TextInput(attrs=({'class': 'form-input'})),
            'pavimentation':  forms.Select(choices=pavimentation_choices, attrs=({'class': 'form-input'})),
            'eletricity':  forms.Select(choices=eletricity_choices, attrs=({'class': 'form-input'})),
            'ilumination':  forms.Select(choices=ilumination_choices, attrs=({'class': 'form-input'})),
            'quantity_houses':  forms.Select(choices=quantity_houses_choices, attrs=({'class': 'form-input'})),
        }
        
        icons = {
            'number':'https://img.icons8.com/?size=48&id=2YHBrgJkUHzJ&format=png',
            'data':'https://img.icons8.com/?size=30&id=ilO1-m5bKBS4&format=png',
            'datetime_created':'https://img.icons8.com/?size=40&id=61987&format=png',
            'local':'https://img.icons8.com/?size=40&id=61987&format=png',
            'bairro':'https://img.icons8.com/?size=48&id=81284&format=png',
            'unidade':'https://img.icons8.com/?size=48&id=80414&format=png',
            'obs':'https://img.icons8.com/?size=48&id=7VIEQ1GiK0Iz&format=png',
            'pavimentation':'https://img.icons8.com/?size=48&id=MEwb2lHaMFxX&format=png',
            'eletricity':'https://img.icons8.com/?size=48&id=xLj25NrPMxFQ&format=png',
            'ilumination':'https://img.icons8.com/?size=48&id=wFfu6zXx15Yk&format=png',
            'quantity_houses':'https://img.icons8.com/?size=64&id=118996&format=png',
            'Reports':'https://img.icons8.com/?size=48&id=11849&format=png',
}

from django import forms
from datetime import datetime
from .models import Certificate
from django.contrib.auth.models import User 

class CertificateForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Usando o widget de data para entrada
        # input_formats=['%d/%m/%Y'],  # Permitindo o formato dd/mm/yyyy
        required=True
    )

    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'}),  # Campo de data com widget DateInput
        }
        
        labels = {'year':'Ano'}
        

    def clean_data(self):
        # Aqui fazemos uma validação manual para garantir que a data seja convertida corretamente
        data = self.cleaned_data.get('data')

        # Se a data não estiver no formato desejado, corrigimos
        if isinstance(data, str):
            try:
                # Tentamos converter para o formato correto: 'dd/mm/yyyy'
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                raise forms.ValidationError("Por favor, informe uma data válida no formato dd/mm/yyyy.")
        
        return data

    # Validação do código (apenas números, sem limitação de tamanho)
    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code.isdigit():
            raise forms.ValidationError("O código deve conter apenas números.")
        return code

    # Validação do CPF/CNPJ com formatação
    def clean_cpf_cnpj(self):
        cpf_cnpj = self.cleaned_data.get('cpf_cnpj')

        if len(cpf_cnpj) == 11:  # CPF
            if not cpf_cnpj.isdigit():
                raise forms.ValidationError("O CPF deve conter apenas números.")
            cpf_cnpj = f"{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}"  # Formata CPF
        elif len(cpf_cnpj) == 14:  # CNPJ
            if not cpf_cnpj.isdigit():
                raise forms.ValidationError("O CNPJ deve conter apenas números.")
            cpf_cnpj = f"{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}"  # Formata CNPJ
        else:
            raise forms.ValidationError("O CPF deve ter 11 dígitos ou o CNPJ 14 dígitos.")
        
        return cpf_cnpj

    # Validação do ano (como número, deve ser um ano válido)
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if isinstance(year, str):  # Se o ano for uma string (caso do DateInput)
            try:
                # Converte a string para um objeto datetime
                year = datetime.strptime(year, "%Y-%m-%d").date()
            except ValueError:
                raise forms.ValidationError("O ano deve ser uma data válida no formato yyyy-mm-dd.")
        
        # Verifica se o ano é um número válido e dentro de um intervalo
        if year.year < 1900 or year.year > datetime.now().year + 1:  # Ajuste do intervalo de anos
            raise forms.ValidationError(f"O ano deve ser entre 1900 e {datetime.now().year + 1}.")
        
        return year

    # Validação do requerente (não pode conter números)
    def clean_requerente(self):
        requerente = self.cleaned_data.get('requerente')
        if any(char.isdigit() for char in requerente):
            raise forms.ValidationError("O nome do requerente não pode conter números.")
        return requerente

    # Validação da latitude (apenas 6 dígitos numéricos)
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if len(latitude) != 6 or not latitude.isdigit():
            raise forms.ValidationError("A latitude deve ter exatamente 6 dígitos numéricos.")
        return latitude

    # Validação da longitude (apenas 8 dígitos numéricos)
    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if len(longitude) != 7 or not longitude.isdigit():
            raise forms.ValidationError("A longitude deve ter exatamente 7 dígitos numéricos.")
        return longitude

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class LoginForm(forms.Form):  # Usamos forms.Form, já que não estamos criando usuários
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário',
            'class': 'form-control',
        }),
        label='Usuário'
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'form-control',
        }),
        label='Senha'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Autentica o usuário
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Usuário ou senha inválidos.")
        self.user = user  # Armazena o usuário autenticado para uso posterior
        return cleaned_data
