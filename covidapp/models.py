from django.db import models

# Create your models here.

class Covid_details(models.Model):
    state_name = models.CharField(max_length=100)
    date_of_record = models.DateField()
    No_of_samples = models.IntegerField()
    no_of_deaths = models.IntegerField()
    no_of_positive = models.IntegerField()
    no_of_negative = models.IntegerField()
    no_of_discharged = models.IntegerField()

    def __str__(self):
        return self.state_name