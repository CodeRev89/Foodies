# Generated by Django 4.1 on 2022-08-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredients",
            name="name",
            field=models.CharField(default=0, max_length=500),
        ),
    ]
