# Generated by Django 5.1.6 on 2025-02-22 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='appointment_files/'),
        ),
    ]
