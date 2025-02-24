# Generated by Django 4.2.1 on 2023-06-16 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "main",
            "0008_rename_admin0_code_iso3_indicator_admin0_code_iso3_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("admin0_code_iso3", models.CharField(max_length=3)),
                ("name", models.CharField(max_length=255)),
                ("iso2", models.CharField(max_length=2)),
            ],
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="meta_data",
            new_name="metadata",
        ),
        migrations.AlterField(
            model_name="metadata",
            name="hdx_id",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name="indicator",
            name="country",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.country",
            ),
        ),
    ]
