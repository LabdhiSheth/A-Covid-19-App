from django.db import models
from django.db.models.deletion import CASCADE

# from Registration_Module.models import CustomUser

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=300)
    phonenumber = models.CharField(max_length=10)
    image = models.ImageField(upload_to = 'hospital_images')
    

    def __str__(self) -> str:
        return self.name

class Resource(models.Model):
    icu_beds = models.IntegerField()
    remdesivir = models.IntegerField()
    vaccine = models.IntegerField()
    ventilators = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=CASCADE, primary_key=True)
    
    def __str__(self) -> str:
        return self.hospital.name

# class Booking(models.Model):
#     icu_beds = models.IntegerField()
#     remdesivir = models.IntegerField()
#     vaccine = models.IntegerField()
#     ventilators = models.IntegerField()
#     hospital = models.ForeignKey(Hospital, on_delete=CASCADE, primary_key=True)
