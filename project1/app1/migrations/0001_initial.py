# Generated by Django 3.0.3 on 2020-04-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=34)),
                ('age', models.CharField(max_length=2)),
                ('address', models.CharField(max_length=34)),
            ],
        ),
    ]
