from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Education(models.Model):
    name=models.CharField(max_length=240)


    def __str__(self) -> str:
        return self.name






    


class Category(models.Model):
    name=models.CharField(max_length=240)
    


    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name=models.CharField(max_length=240)  


    def __str__(self) -> str:
        return self.name

class Salary(models.Model):
    name =models.CharField(max_length=240)

    def __str__(self) -> str:
        return self.name

class Job(models.Model):
    company_name=models.CharField(max_length=240)
    title=models.CharField(max_length=240)
    category=models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, null=True)
    location=models.ForeignKey(to=Location, on_delete=models.CASCADE, null=True)
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    salary=models.CharField(max_length=240)
    descript=models.TextField()
    contact=models.CharField(max_length=240)
    education=models.ForeignKey(to=Education, on_delete=models.CASCADE, null=True)


    created = models.DateTimeField(auto_created=True, null=True)



    
    


    def __str__(self) -> str:
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=240)
    reciever = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    messege=models.TextField()
    contact = models.CharField(max_length=240)



