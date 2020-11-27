from django.db import models

# Create your models here.

class Coursedetails(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=100)
    coursename = models.CharField(max_length=150)
    section = models.IntegerField() 
    coursedepartment = models.CharField(max_length=100)
    instructorfullname = models.CharField(max_length=300)



class Studentdetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    major = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    gpa = models.DecimalField(decimal_places=2,max_digits=3)


class Enrollment(models.Model):
    firstname = models.CharField(max_length=150)
    course = models.CharField(max_length=150)