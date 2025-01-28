from django.db import models
import django
import datetime
from ProjetoCA.settings import BASE_DIR, MEDIA_ROOT
from django.contrib.auth.models import User

today = datetime.date.today()
# Create your models here.
class Report(models.Model):
    number = models.CharField(max_length=10)
    data = models.DateField(default=django.utils.timezone.now)
    datetime_created = models.DateTimeField(auto_created=True, auto_now_add= True)
    local = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    unidade = models.CharField(max_length=255, null = True, blank=True)
    obs  = models.CharField(max_length=25, null = True, blank=True)
    pavimentation = models.CharField(max_length=255)
    eletricity = models.CharField(max_length=255)
    ilumination = models.CharField(max_length=255)
    quantity_houses = models.CharField(max_length=255)
    photos = models.ImageField(default='404.png')
    Reports = models.CharField(max_length=600, blank=True, default='Não há relatórios')
    
    def __str__(self) -> str:
        return self.number
    
class Report_fisico(models.Model):
    number = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    
    local = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    
    requerente = models.CharField(max_length=255, null = True)
    cpf_cnpj  = models.CharField(max_length=25, null = True)
    
    data = models.DateField(default=django.utils.timezone.now)
    unidade = models.CharField(max_length=255)
    
    
    pavimentation = models.CharField(max_length=255)
    ilumination = models.CharField(max_length=255)
    
    
    eletricity = models.CharField(max_length=255)
    quantity_houses = models.CharField(max_length=255)
    
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    
    photos = models.ImageField(default='404.png')
    Reports = models.CharField(max_length=600, blank=True, default='Não há relatórios')
    
    # datetime_created = models.DateTimeField(auto_created=True, auto_now_add= True)
    def __str__(self) -> str:
        return self.number

class Certificate(models.Model):
    code = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    year = models.CharField(max_length=255)
    requerente = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    data = models.CharField(max_length=255)