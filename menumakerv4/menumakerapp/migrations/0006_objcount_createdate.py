# Generated by Django 3.1.5 on 2021-03-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menumakerapp', '0005_objcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='objcount',
            name='createDate',
            field=models.CharField(default='', editable=False, max_length=15),
        ),
    ]
