# Generated by Django 4.2.3 on 2023-08-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0018_notes_subject_alter_notes_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
