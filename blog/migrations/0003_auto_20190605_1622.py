# Generated by Django 2.2 on 2019-06-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190513_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(default=None, max_length=5000),
        ),
    ]
