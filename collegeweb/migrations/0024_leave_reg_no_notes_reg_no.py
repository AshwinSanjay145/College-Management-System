# Generated by Django 4.2.3 on 2023-09-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0023_notices'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='reg_no',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='reg_no',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
