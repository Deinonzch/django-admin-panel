# Generated by Django 2.1.2 on 2018-10-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_myadminpanel_app_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myadminpanel',
            name='app_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='myadminpanel',
            name='model_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]