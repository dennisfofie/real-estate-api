# Generated by Django 4.1.7 on 2023-03-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("real_estate", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/profile_pic/"
            ),
        ),
    ]
