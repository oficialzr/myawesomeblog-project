# Generated by Django 4.1.7 on 2023-03-08 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_text',
            field=models.CharField(max_length=200),
        ),
    ]