# Generated by Django 3.2.9 on 2021-11-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('row', '0004_auto_20211126_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
