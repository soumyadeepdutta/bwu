# Generated by Django 3.1.3 on 2020-11-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201122_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='limitations',
            field=models.CharField(blank=True, default='', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='specifications',
            field=models.CharField(blank=True, default='', max_length=1024, null=True),
        ),
    ]