# Generated by Django 4.0.5 on 2022-06-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='presentation',
            field=models.FileField(null=True, upload_to='presentations/'),
        ),
    ]