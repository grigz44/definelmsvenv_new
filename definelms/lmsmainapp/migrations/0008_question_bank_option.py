# Generated by Django 4.1.1 on 2022-10-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0007_alter_exam_question_allocation_exam_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_bank',
            name='option',
            field=models.CharField(default='', max_length=5000),
        ),
    ]