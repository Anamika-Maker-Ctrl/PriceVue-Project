# Generated by Django 3.2.5 on 2023-09-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
