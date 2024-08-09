from django.db import models

# Create your models here.
class Congregation(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'tb_congregation'


class Religion(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'tb_religion'



class Sacrament(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'tb_sacrament'
    