# Generated by Django 2.2.9 on 2020-07-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piroquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=800, verbose_name='퀴즈제목')),
            ],
        ),
    ]
