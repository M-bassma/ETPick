# Generated by Django 3.0.5 on 2020-05-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('ville', models.TextField(null=True)),
                ('pays', models.CharField(max_length=100)),
                ('email', models.TextField(null=True)),
                ('company', models.CharField(max_length=100)),
                ('aboutMe', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'recruteur',
                'ordering': ['nom'],
            },
        ),
    ]
