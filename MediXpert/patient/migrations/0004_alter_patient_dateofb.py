# Generated by Django 3.2.7 on 2022-11-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_rename_dob_patient_dateofb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dateofb',
            field=models.CharField(max_length=30),
        ),
    ]
