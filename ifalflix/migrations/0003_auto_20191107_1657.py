# Generated by Django 2.2.3 on 2019-11-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifalflix', '0002_auto_20191106_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='series',
            name='banner',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='temp',
            field=models.IntegerField(),
        ),
    ]