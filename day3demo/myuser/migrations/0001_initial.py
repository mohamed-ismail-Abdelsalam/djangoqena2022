# Generated by Django 4.0.5 on 2022-06-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=10)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]