# Generated by Django 4.1.7 on 2023-03-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("real_estate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
