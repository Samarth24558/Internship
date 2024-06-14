# Generated by Django 5.0.6 on 2024-06-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('rm', models.CharField(max_length=200, null=True)),
                ('item', models.CharField(max_length=200, null=True)),
                ('details', models.CharField(max_length=200, null=True)),
                ('qty', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]