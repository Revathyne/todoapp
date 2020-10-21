from django.db import models

# Create your models here.containing essential field and behaviour
class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text