# Generated by Django 4.2.1 on 2023-06-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_mobile_profile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=29, verbose_name=''),
        ),
    ]
