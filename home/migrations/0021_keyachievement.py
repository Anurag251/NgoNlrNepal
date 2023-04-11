# Generated by Django 4.0.4 on 2022-08-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_messagefromdirector_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='about/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Key Achievement',
            },
        ),
    ]