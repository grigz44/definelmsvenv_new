# Generated by Django 4.1.1 on 2023-02-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0003_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isdemanded',
            field=models.BooleanField(default=True),
        ),
    ]