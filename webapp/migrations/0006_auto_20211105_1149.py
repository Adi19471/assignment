# Generated by Django 3.2.9 on 2021-11-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20211105_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='date_of_assigning_task',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='date_of_call_to_people',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='date_of_submistion',
            field=models.DateField(),
        ),
    ]
