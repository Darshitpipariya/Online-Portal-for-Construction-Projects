# Generated by Django 3.1.3 on 2021-03-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0018_auto_20210316_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastproject',
            name='project_name',
            field=models.CharField(max_length=255),
        ),
    ]