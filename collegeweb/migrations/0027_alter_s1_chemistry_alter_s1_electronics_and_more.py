# Generated by Django 4.2.3 on 2023-09-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0026_s1_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1',
            name='chemistry',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1',
            name='electronics',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1',
            name='graphics',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1',
            name='mathematics',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1',
            name='physics',
            field=models.CharField(max_length=8),
        ),
    ]
