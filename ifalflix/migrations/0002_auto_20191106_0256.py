# Generated by Django 2.2.3 on 2019-11-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifalflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='temp',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
