# Generated by Django 4.1.4 on 2022-12-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0018_dbook_refer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='bloodp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='chol',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='cpain',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='cpaintype',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='ecg',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='fasting',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='heart',
            field=models.IntegerField(default=0),
        ),
    ]