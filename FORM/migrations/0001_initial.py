# Generated by Django 5.0.7 on 2024-08-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('mailing_address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('identification_document', models.FileField(upload_to='identification_documents/')),
            ],
        ),
    ]
