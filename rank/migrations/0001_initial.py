# Generated by Django 3.2.9 on 2021-11-24 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hall.hall')),
            ],
            options={
                'unique_together': {('hall', 'name')},
            },
        ),
    ]
