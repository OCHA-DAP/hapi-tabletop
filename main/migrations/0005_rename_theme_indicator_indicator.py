# Generated by Django 4.2.1 on 2023-05-24 10:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_indicator_value"),
    ]

    operations = [
        migrations.RenameField(
            model_name="indicator",
            old_name="Theme",
            new_name="Indicator",
        ),
    ]
