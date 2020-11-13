# Generated by Django 3.1.3 on 2020-11-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BecomeAnAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('location', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Become Agents',
            },
        ),
        migrations.CreateModel(
            name='FindAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('location', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Finding Agents',
            },
        ),
        migrations.CreateModel(
            name='FindHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.TextField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Finding Home',
            },
        ),
        migrations.CreateModel(
            name='GeneralEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.TextField(max_length=255)),
                ('query', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'General Queries',
            },
        ),
        migrations.CreateModel(
            name='SellHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('location', models.TextField(max_length=255)),
                ('age', models.FloatField()),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Selling Home',
            },
        ),
    ]
