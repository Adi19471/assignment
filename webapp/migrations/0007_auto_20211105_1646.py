# Generated by Django 3.2.9 on 2021-11-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20211105_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='call_to_people',
        ),
        migrations.AddField(
            model_name='assignments',
            name='call_to_people',
            field=models.ManyToManyField(to='webapp.Employe'),
        ),
    ]
