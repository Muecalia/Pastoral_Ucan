from django.db import models

# Create your models here.
class Country(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    nationality = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "tb_country"
        ordering = ['-description']

class Province(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "tb_province"
        ordering = ['-description']


class County(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "tb_county"
        ordering = ['-description']

