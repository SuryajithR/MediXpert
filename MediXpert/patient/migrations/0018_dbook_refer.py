# Generated by Django 4.1.4 on 2022-12-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_testresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbook',
            name='refer',
            field=models.BooleanField(default=True),
        ),
    ]