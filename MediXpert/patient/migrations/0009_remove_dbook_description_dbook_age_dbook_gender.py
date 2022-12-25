# Generated by Django 4.1.3 on 2022-12-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_dbook_alter_doctor_id_alter_patient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbook',
            name='description',
        ),
        migrations.AddField(
            model_name='dbook',
            name='age',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dbook',
            name='gender',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
