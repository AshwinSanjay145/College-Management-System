# Generated by Django 4.2.3 on 2023-09-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeweb', '0021_alter_notes_upload_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFile',
        ),
        migrations.AlterField(
            model_name='notes',
            name='upload_date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
