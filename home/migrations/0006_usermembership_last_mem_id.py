# Generated by Django 2.0.3 on 2019-04-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190402_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='last_mem_id',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
