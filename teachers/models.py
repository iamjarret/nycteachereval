from django.db import models

class School(models.Model):
    dbn = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=100, blank = True, null=True)
    freelunch = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sped = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ell = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    asian = models.DecimalField(max_digits=4,   decimal_places=1, blank=True, null=True)
    black = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hisp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    white = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    male = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    female = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    overall_grade = models.CharField(max_length=1, blank=True, null=True)
    dropout = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ['name']

class Teachers(models.Model):
    teacherid = models.CharField(max_length=100, unique=True)
    dbn = models.ForeignKey(School, to_field='dbn')
    va_0910_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0910_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0809_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0809_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0708_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0708_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0607_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    va_0607_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    
    class Meta:
        ordering = ['dbn']