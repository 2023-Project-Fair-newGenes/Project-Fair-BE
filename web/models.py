from django.db import models

class GenomeCharacteristics(models.Model):
    snp_id = models.TextField(primary_key=True)
    snp_name = models.TextField()
    characteristics = models.TextField()


class LifestyleInformation(models.Model):
    snp_id = models.ForeignKey("GenomeCharacteristics", on_delete=models.CASCADE)
    info = models.TextField()
