# Generated by Django 4.2.5 on 2023-10-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20231024_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=100, verbose_name='Логин'),
        ),
    ]
