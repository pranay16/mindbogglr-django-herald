# Generated by Django 2.2.1 on 2019-05-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herald', '0008_auto_20190503_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentnotification',
            name='receiver_doctor_profile_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
