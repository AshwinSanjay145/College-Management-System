# Generated by Django 4.2.3 on 2023-08-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0017_alter_notes_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='semester',
            field=models.CharField(max_length=10),
        ),
    ]