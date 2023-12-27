from django.contrib import admin
from . import models

class ProfessionalAdmin(admin.ModelAdmin):
  list_display = ["name", "avatar", "date_joined", "active"]
  list_editable= ["active"]


admin.site.register(models.Services)
admin.site.register(models.Cities)
admin.site.register(models.Professional, ProfessionalAdmin)