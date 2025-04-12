from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class StudentSub(models.Model):
    subname = models.CharField(max_length=100)
    sid = models.IntegerField()

    def __str__(self):
        return self.subname
