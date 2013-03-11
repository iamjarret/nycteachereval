from django.db import models

class Distribution(models.Model):
    '''
    The idea of this class is to store distribution data i.e. class size distribution data

    values would be class sizes
    dist would be number of kids in a class that size
    and total num would be total number of kids

    *dividing total number of kids in each class that size by total number of kids gives the
    percentage of kids in that category
    '''
    name = models.CharField(max_length=100, unique=True)
    values = models.CommaSeparatedIntegerField(max_length=10, blank=True, null=True)
    dist = models.CommaSeparatedIntegerField(max_length=10, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=100, unique=True)

class District(models.Model):
    name = models.CharField(max_length=2, unique=True)
    classsize_dist = models.ForeignKey(Distribution, to_field='name', blank=True, null=True)
    avgclasssize = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True) #API working

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    classsize_dist = models.ForeignKey(Distribution, to_field='name', blank=True, null=True)
    avgclasssize = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Borough(models.Model):
    name = models.CharField(max_length=100, unique=True)
    classsize_dist = models.ForeignKey(Distribution, to_field='name', blank=True, null=True)
    avgclasssize = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __unicode__(self):
        return self.name

class School(models.Model):
    dbn = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=100, blank = True, null=True)
    
    #contact, location
    address = models.CharField(max_length=100, blank = True, null=True)
    phone = models.IntegerField(max_length=10, blank=True, null=True) 
    email = models.EmailField(max_length=100, blank = True, null=True)
    url = models.URLField(max_length=100, blank = True, null=True)
    district = models.ForeignKey(District, to_field='name')
    city = models.ForeignKey(City, to_field='name')
    borough = models.ForeignKey(Borough, to_field='name')
    zipcode = models.IntegerField(max_length=5, blank=True, null=True)
    x_geo = models.FloatField(blank=True, null=True)
    y_geo = models.FloatField(blank=True, null=True)

    #administative
    principal = models.CharField(max_length=100, blank = True, null=True)
    
    #demographics
    freelunch = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sped = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ell = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    asian = models.DecimalField(max_digits=4,   decimal_places=1, blank=True, null=True)
    black = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hisp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    white = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    male = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    female = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    size = models.IntegerField(max_length=5, blank = True, null=True) #API working
    schooltype = models.CharField(max_length=20, blank = True, null=True)
    dropout = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    avgclasssize = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True) #API working
    teachpupilratio = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True) #API working

    #published evaluations
    reportcardgrade = models.CharField(max_length=1, blank=True, null=True)
    reportcardgrade_adj = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s: %s"%(self.dbn, self.name)

class Teachers(models.Model):
    teacherid = models.CharField(max_length=100, unique=True)
    school = models.ForeignKey(School, to_field='dbn')
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
        ordering = ['last_name']

    def __unicode__(self):
        return "%s, %s"%(self.last_name, self.first_name)