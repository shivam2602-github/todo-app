from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name= models.CharField(max_length=50)
    address=models.TextField()
    no=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()

