# Generated by Django 4.0.2 on 2022-03-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projects_delete_project_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.CharField(max_length=800)),
            ],
        ),
    ]
