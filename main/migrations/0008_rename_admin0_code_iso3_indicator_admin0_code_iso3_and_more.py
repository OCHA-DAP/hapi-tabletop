# Generated by Django 4.2.1 on 2023-06-15 11:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_metadata_indicator_metadata"),
    ]

    operations = [
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin0_Code_ISO3",
            new_name="admin0_code_iso3",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin1_Code",
            new_name="admin1_code",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin1_Name",
            new_name="admin1_name",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin2_Code",
            new_name="admin2_code",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin2_Name",
            new_name="admin2_name",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin3_Code",
            new_name="admin3_code",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin3_Name",
            new_name="admin3_name",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin4_Code",
            new_name="admin4_code",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Admin4_Name",
            new_name="admin4_name",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Date",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Indicator",
            new_name="indicator_name",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Key",
            new_name="key",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Lat",
            new_name="lat",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Lng",
            new_name="lng",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="MetaData",
            new_name="meta_data",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Record_ID",
            new_name="record_id",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Record_Source",
            new_name="record_source",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="Value",
            new_name="value",
        ),
    ]
