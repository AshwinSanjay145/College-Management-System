# Generated by Django 4.2.3 on 2023-08-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0006_alter_students_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='semaster',
            field=models.CharField(max_length=2),
        ),
    ]
