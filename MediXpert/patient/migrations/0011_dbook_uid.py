# Generated by Django 4.1.4 on 2022-12-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_alter_dbook_btime'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbook',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]