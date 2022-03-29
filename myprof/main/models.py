import email
from email.mime import image
from tkinter.tix import Tree
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.

# Certificate Section

class certificates(models.Model):
    # id = models.Count()
    image = models.ImageField(upload_to='main/static/certificates')
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.description


# Project Section With Filter tag

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    image = models.ImageField(upload_to='main/static/Projects')
    title = models.CharField(max_length=200, db_index=True)
    project_title = models.CharField(max_length=200, db_index=True)
    tags = models.ManyToManyField(Tag)
    github_urls = models.CharField(max_length=300, null=True)
    youtube_urls = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title



# Contact Section for saving the contact messages

class contactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.CharField(max_length=800)

    def __str__(self):
        return self.name
