# Generated by Django 2.2 on 2019-04-19 02:57

from django.db import migrations, models
import social_network.models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0003_auto_20190418_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='headshot',
            field=models.ImageField(blank=True, null=True, upload_to=social_network.models.headshot_file_name),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=social_network.models.resume_file_name),
        ),
    ]