# Generated by Django 4.2.7 on 2023-11-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='type',
            field=models.CharField(choices=[('OFFER', 'OFFER'), ('CATEGORY', 'CATEGORY')], max_length=100),
        ),
    ]