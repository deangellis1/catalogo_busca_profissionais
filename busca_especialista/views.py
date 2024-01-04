from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
import re

from .models import *


def professional_list(request):
    professional_list = Professional.objects.filter(active=True).order_by('-instagram_user')
    services = Services.objects.all().order_by('service')
    cities = Cities.objects.all().order_by('city_name')

    paginator = Paginator(professional_list, 12)

    page = request.GET.get('page')
    professionals = paginator.get_page(page)

    context = { "professionals": professionals, "services": services, "cities": cities }

    return render(request, "busca_especialista/professional_list.html", context)


def filter_professionals(request):
    
    if request.method == 'POST':
        servico_selecionado = request.POST.get('service')
        cidade_selecionada = request.POST.get('city')

        if servico_selecionado == '18':
            filtered_professionals = Professional.objects.filter(
            active=True,
            cities_attended=cidade_selecionada)
            return render(request, 'busca_especialista/results.html', {'filtered_professionals': filtered_professionals})

        filtered_professionals = Professional.objects.filter(
            active=True,
            services_provided=servico_selecionado,
            cities_attended=cidade_selecionada)
        return render(request, 'busca_especialista/results.html', {'filtered_professionals': filtered_professionals})


def about(request):
    return render(request, "busca_especialista/about.html")


def details(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    context = {"professional": professional}
    return render(request, "busca_especialista/details.html", context)

"""
class ProfessionalListView(ListView):
    model = Professional
    queryset = Professional.objects.filter(active=True)
"""


class ServicesListView(ListView):
    model = Services
    

class ProfessionalCreateView(CreateView):
    model = Professional
    fields = ["name", "whatsapp_number", "instagram_user", "email", "services_provided", "cities_attended", "avatar"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Obtém o número do WhatsApp do formulário e remove caracteres não numéricos
        whatsapp_number = form.cleaned_data['whatsapp_number']
        only_numbers = re.sub(r'\D', '', whatsapp_number)  # Remove tudo que não é dígito
        form.instance.whatsapp_number = only_numbers
        
        return super(ProfessionalCreateView, self).form_valid(form)


"""
class ProfessionalCreateView(CreateView):
    model = Professional
    fields = ["name", "whatsapp_number", "instagram_user", "email", "services_provided", "cities_attended", "avatar"]
    success_url = reverse_lazy("home")

"""