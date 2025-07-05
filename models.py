from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    desc = models.TextField(max_length=500)
    date   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.email