from django.db import models

# Create your models here.


class indicator(models.Model):
    Admin0_Code_ISO3 = models.CharField(max_length=3)
    Admin1_Name = models.CharField(max_length=255, null=True)
    Admin1_Code = models.CharField(max_length=20, null=True)
    Admin2_Name = models.CharField(max_length=255, null=True)
    Admin2_Code = models.CharField(max_length=20, null=True)
    Admin3_Name = models.CharField(max_length=255, null=True)
    Admin3_Code = models.CharField(max_length=20, null=True)
    Admin4_Name = models.CharField(max_length=255, null=True)
    Admin4_Code = models.CharField(max_length=20, null=True)
    Lat = models.CharField(max_length=20, null=True)
    Lng = models.CharField(max_length=20, null=True)
    Record_ID = models.IntegerField()
    Record_Source = models.CharField(max_length=255)
    Indicator = models.CharField(max_length=255)
    Key = models.CharField(max_length=255)
    Value = models.CharField(max_length=255, null=True)
