from django.urls import path
from busca_especialista.views import professional_list, filter_professionals, about, details, ProfessionalCreateView, ServicesListView

urlpatterns = [
    path("", professional_list, name="home"),
    path("results", filter_professionals, name="results"),
    path("about", about, name="about"),
    path("details/<int:professional_id>", details, name="details"),
    path("services", ServicesListView.as_view(), name="services"),
    path("register", ProfessionalCreateView.as_view(), name="register")
]