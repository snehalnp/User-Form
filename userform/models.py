from django.db import models

# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
