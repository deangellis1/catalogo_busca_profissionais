from django.db import models

# Create your models here.

class Services(models.Model):
    service = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=240, null=True, blank=True)

    def __str__(self):
        return self.service

class Cities(models.Model):
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

class Professional(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50)
    whatsapp_number = models.CharField(verbose_name="Whatsapp",max_length=11)
    instagram_user = models.CharField(verbose_name="Instagram",max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name="E-mail", max_length=30, null=True, blank=True)
    services_provided = models.ManyToManyField(Services, verbose_name="Serviços Prestados")
    cities_attended = models.ManyToManyField(Cities, verbose_name="Cidades Atendidas")
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
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