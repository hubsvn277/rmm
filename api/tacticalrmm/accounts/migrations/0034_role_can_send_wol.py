# Generated by Django 4.1.9 on 2023-05-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0033_user_dash_info_color_user_dash_negative_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="can_send_wol",
            field=models.BooleanField(default=False),
        ),
    ]
