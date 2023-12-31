# Generated by Django 4.2.3 on 2023-08-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('reg_no', models.IntegerField(max_length=6)),
                ('semaster', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('place', models.CharField(max_length=200, null=True)),
                ('guardian_phone', models.IntegerField(max_length=12, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
