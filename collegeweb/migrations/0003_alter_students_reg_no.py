# Generated by Django 4.2.3 on 2023-08-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0002_alter_students_guardian_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='reg_no',
            field=models.IntegerField(),
        ),
    ]