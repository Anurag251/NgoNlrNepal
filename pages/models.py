from django.db import models

# Create your models here.

class Donation(models.Model):
    fullname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    receipt = models.FileField(upload_to='donation/', max_length=200)

    class Meta:
        verbose_name = ("Donation")
        verbose_name_plural = ("Donations")

    def __str__(self):
        return self.fullname
