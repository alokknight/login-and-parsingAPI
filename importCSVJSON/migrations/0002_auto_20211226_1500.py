# Generated by Django 3.1.13 on 2021-12-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importCSVJSON', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='csvs'),
        ),
    ]