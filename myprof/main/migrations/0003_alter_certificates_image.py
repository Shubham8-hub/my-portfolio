# Generated by Django 4.0.2 on 2022-03-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificates_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=models.ImageField(upload_to='main/static/certificates'),
        ),
    ]
