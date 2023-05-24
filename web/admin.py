from django.contrib import admin
from .models import GenomeCharacteristics, LifestyleInformation, SNPGenotype

admin.site.register(GenomeCharacteristics)
admin.site.register(LifestyleInformation)
admin.site.register(SNPGenotype)