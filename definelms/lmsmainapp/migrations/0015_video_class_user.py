# Generated by Django 4.1.1 on 2022-12-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0014_video_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_class',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lmsmainapp.login'),
            preserve_default=False,
        ),
    ]
