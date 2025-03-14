# Generated by Django 5.1.5 on 2025-03-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_images/'),
        ),
    ]
