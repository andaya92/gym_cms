# Generated by Django 2.0.3 on 2019-04-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190401_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipplan',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
