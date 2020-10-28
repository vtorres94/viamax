# Generated by Django 3.1.2 on 2020-10-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_base64', models.CharField(max_length=64)),
                ('pagador', models.CharField(max_length=80)),
                ('tipo_cambio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]