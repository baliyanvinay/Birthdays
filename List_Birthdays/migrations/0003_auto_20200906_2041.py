# Generated by Django 3.1 on 2020-09-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List_Birthdays', '0002_auto_20200906_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_birthdays',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
