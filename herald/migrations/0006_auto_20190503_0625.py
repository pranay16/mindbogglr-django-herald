# Generated by Django 2.2.1 on 2019-05-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herald', '0005_auto_20180516_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentnotification',
            name='sender_doctor_profile_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='sentnotification',
            index=models.Index(fields=['sender_doctor_profile_id'], name='herald_sent_sender__1d4af5_idx'),
        ),
    ]
