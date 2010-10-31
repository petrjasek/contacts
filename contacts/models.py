from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    mobil = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    web = models.URLField(blank=True)
    comment = models.TextField(blank=True)
    ico = models.CharField(max_length=12, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.firstname, self.surname)

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    ico = models.CharField(max_length=12, blank=True)
    dic = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    web = models.URLField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    fax = models.CharField(max_length=50, blank=True)
    persons = models.ManyToManyField(Person, blank=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    companies = models.ManyToManyField(Company, blank=True)
    persons = models.ManyToManyField(Person, blank=True)

    def __unicode__(self):
        return self.name

