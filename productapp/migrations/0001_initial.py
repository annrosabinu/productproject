# Generated by Django 5.1.3 on 2024-12-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255, null=True)),
                ('productdescription', models.CharField(max_length=255, null=True)),
                ('productquantity', models.CharField(max_length=255, null=True)),
                ('productprice', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
