# Generated by Django 4.0.4 on 2022-09-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_ourpartnerdatas'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]