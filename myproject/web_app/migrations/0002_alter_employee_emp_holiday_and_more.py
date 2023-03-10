# Generated by Django 4.1.7 on 2023-02-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_holiday',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_holiday_approved',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_holiday_pending',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_holiday_reject',
            field=models.IntegerField(max_length=5),
        ),
    ]
