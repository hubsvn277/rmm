# Generated by Django 3.2.6 on 2021-09-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0011_auto_20210731_1707"),
    ]

    operations = [
        migrations.AlterField(
            model_name="script",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="script",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]