# Generated by Django 4.1 on 2023-02-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
