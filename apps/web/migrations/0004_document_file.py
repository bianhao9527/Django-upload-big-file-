# Generated by Django 2.0.3 on 2018-04-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_document_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]