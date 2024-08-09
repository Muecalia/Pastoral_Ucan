from django.db import models

# Create your models here.
class AcademicLevel(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tb_academic_level'


class TypeActivity(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tb_type_activity'


