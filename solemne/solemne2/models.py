# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone


@python_2_unicode_compatible 
class Contractor(models.Model):
    #project
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=2, blank=True)
    created_by = models.ForeignKey(User, related_name='Contractor_created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(User, related_name='Contractor_modified_by')
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible  
class Project(models.Model):
    name = models.CharField(max_length=50)
    jobNumber = models.CharField(max_length=8)
    shopOut = models.DateTimeField(null=True)
    shopIn = models.DateTimeField(null=True)
    delivery = models.DateTimeField(null=True)
    job1 = models.CharField(max_length=50, null=True)
    job2 = models.CharField(max_length=50, null=True)
    job3 = models.CharField(max_length=50, null=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, default=101)
    created_by = models.ForeignKey(User, related_name='Project_created_by')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, related_name='Project_modified_by')
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_by = User.objects.get(id=1)
            self.modified_by = User.objects.get(id=1)
            super(Project, self).save(*args, **kwargs)
            year = datetime.datetime.now().year
            self.jobNumber = '{}{:04d}'.format(year, self.id)
        self.modified_by = User.objects.get(id=1)
        super(Project, self).save(*args, **kwargs)