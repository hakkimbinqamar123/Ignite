from django.db import models
from datetime import date, time
from django import forms
from django.contrib.auth.models import User

# Create your models here.\

class Event(models.Model):
    event_id=models.IntegerField("Id of user", primary_key=True)
    pgm_name = models.CharField("prog_name", max_length=30)
    venue_name=models.CharField("venue_name", max_length=30, default="block A")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='images', default=0)
    about = models.CharField(max_length=500, default=0)
    description = models.CharField(max_length=500, default=0)
    heading = models.CharField(max_length=50)
    rate = models.IntegerField()
    status = models.CharField("status",max_length=30, null=True)

    def __str__(self):
        return self.pgm_name


class Student(models.Model):
    candidate_id=models.IntegerField("Id of user", primary_key=True)
    username=models.CharField("Name of user", max_length=50)
    email=models.EmailField("Email")
    phone=models.IntegerField("Phone number")
    password = models.CharField("Password", max_length=25)
    college = models.CharField("college", max_length=100)
    id_card = models.ImageField(upload_to='images')
    events = models.ManyToManyField(Event, blank=True)



    def __str__(self):
        return self.username

     
class Judge(models.Model):
    j_id=models.IntegerField("Id of user", primary_key=True)
    event=models.ForeignKey(Event,models.CASCADE, null=True,blank=True)
    username=models.CharField("Name of user", max_length=50)
    email=models.EmailField("Email")
    phone=models.IntegerField("Phone number") 
    password = models.CharField("Password", max_length=25)
    qualification = models.CharField("Qualification", max_length=25)

    def __str__(self):
        return self.username
    

    
class Result(models.Model):
    event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
    candidate_id=models.IntegerField(default=1)
    position=models.IntegerField("position of candidate")
    grade=models.CharField("grade of candidate", max_length=10)
    j_id=models.ForeignKey(Judge, on_delete=models.CASCADE)

    def __str__(self):
        return f"Event: {self.event_id}"



class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    