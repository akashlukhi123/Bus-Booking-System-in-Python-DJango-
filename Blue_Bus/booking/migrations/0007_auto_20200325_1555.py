# Generated by Django 3.0.2 on 2020-03-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20200324_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger_detail',
            old_name='zender',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='passenger_detail',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]
