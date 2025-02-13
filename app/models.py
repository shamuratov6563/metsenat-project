from django.db import models


# Django ORM 
# Model == Table in database
class Person(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='person/', null=True, blank=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=200, null=True)
    

class StudentPoint(models.Model):
    student = models.ForeignKey(Person, on_delete=models.PROTECT) 
    point = models.CharField(max_length=300)
