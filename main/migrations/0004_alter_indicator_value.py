# Generated by Django 4.2.1 on 2023-05-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_indicator_admin1_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indicator",
            name="Value",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
