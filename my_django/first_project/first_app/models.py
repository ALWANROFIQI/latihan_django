from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    name = models. CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete= models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    date = models.DateField()

    def __str__(self):
         return f"Access by {self.person.name if self.person else 'Unknown'} on {self.date}"
    
