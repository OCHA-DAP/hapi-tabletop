from django.db import models


class MetaData(models.Model):
    indicator_name = models.CharField(max_length=255)
    hdx_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    dataset_source = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    dataset_date_range = models.CharField(max_length=50)
    last_modified = models.DateTimeField()
    data_update_frequency = models.CharField(max_length=255)


class Indicator(models.Model):
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
    Date = models.DateField(null=True)
    Record_ID = models.IntegerField()
    Record_Source = models.CharField(max_length=255)
    Indicator = models.CharField(max_length=255)
    Key = models.CharField(max_length=255)
    Value = models.CharField(max_length=255, null=True)
    MetaData = models.ForeignKey(
        MetaData, on_delete=models.SET_NULL, null=True
    )
