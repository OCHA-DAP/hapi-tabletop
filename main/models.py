from django.db import models


class MetaData(models.Model):
    indicator_name = models.CharField(max_length=255)
    hdx_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    dataset_source = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    dataset_date_range = models.CharField(max_length=50)
    last_modified = models.DateTimeField()
    data_update_frequency = models.CharField(max_length=255)


class Country(models.Model):
    admin0_code_iso3 = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    iso2 = models.CharField(max_length=2)


class Indicator(models.Model):
    admin0_code_iso3 = models.CharField(max_length=3)
    admin1_name = models.CharField(max_length=255, null=True)
    admin1_code = models.CharField(max_length=20, null=True)
    admin2_name = models.CharField(max_length=255, null=True)
    admin2_code = models.CharField(max_length=20, null=True)
    admin3_name = models.CharField(max_length=255, null=True)
    admin3_code = models.CharField(max_length=20, null=True)
    admin4_name = models.CharField(max_length=255, null=True)
    admin4_code = models.CharField(max_length=20, null=True)
    lat = models.CharField(max_length=20, null=True)
    lng = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    record_id = models.IntegerField()
    record_source = models.CharField(max_length=255)
    indicator_name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, null=True)
    metadata = models.ForeignKey(
        MetaData, on_delete=models.SET_NULL, null=True
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
