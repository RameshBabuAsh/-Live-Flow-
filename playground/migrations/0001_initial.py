# Generated by Django 4.2 on 2023-04-09 10:32

from django.db import migrations, models
import playground.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500)),
                ('Video', models.FileField(upload_to='playground/media/%y', validators=[playground.validators.file_size])),
            ],
        ),
    ]
