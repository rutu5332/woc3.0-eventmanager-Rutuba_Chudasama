# Generated by Django 3.1.5 on 2021-01-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('descriptio', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('fromdate', models.DateField()),
                ('fromtime', models.CharField(max_length=10)),
                ('todate', models.DateField()),
                ('totime', models.CharField(max_length=10)),
                ('enddate', models.DateField()),
                ('endtime', models.CharField(max_length=10)),
                ('host_email', models.EmailField(max_length=254)),
                ('host_pass', models.CharField(max_length=15)),
            ],
        ),
    ]
