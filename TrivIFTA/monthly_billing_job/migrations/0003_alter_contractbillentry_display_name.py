# Generated by Django 4.2.8 on 2024-02-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monthly_billing_job", "0002_alter_contractbillentry_assigned_po_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contractbillentry",
            name="display_name",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
