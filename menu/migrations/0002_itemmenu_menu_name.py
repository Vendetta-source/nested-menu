# Generated by Django 4.1.4 on 2022-12-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmenu',
            name='menu_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название меню'),
        ),
    ]
