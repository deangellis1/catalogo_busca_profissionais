from django.db import models

# Create your models here.

class Services(models.Model):
    service = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.service

class Cities(models.Model):
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

class Professional(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50, help_text="Digite seu nome completo")
    whatsapp_number = models.CharField(verbose_name="Whatsapp",max_length=15, help_text="Digite o seu número de WhatsApp/Telefone")
    instagram_user = models.CharField(verbose_name="Instagram",max_length=30, null=True, blank=True, help_text="Digite o seu nome de usuário no Instagram sem o @")
    email = models.EmailField(verbose_name="E-mail", max_length=50, null=True, blank=True, help_text="Informe o seu e-mail")
    services_provided = models.ManyToManyField(Services, verbose_name="Serviços Prestados", help_text="Se estiver no computador, segure a tecla Ctrl para selecionar mais de uma opção")
    cities_attended = models.ManyToManyField(Cities, verbose_name="Cidades Atendidas", help_text="Se estiver no computador, segure a tecla Ctrl para selecionar mais de uma opção")
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True, help_text="Escolha uma imagem que represente o seu trabalho")
    num_stars = models.IntegerField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
"""
class Phone(models.Model):
    phone_number = models.CharField(max_length=11)
    contact = models.ForeignKey(Professional, on_delete=models.CASCADE)

    """