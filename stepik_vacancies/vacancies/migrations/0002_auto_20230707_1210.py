# Generated by Django 3.2.20 on 2023-07-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
