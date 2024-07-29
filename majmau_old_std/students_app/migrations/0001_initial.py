# Generated by Django 5.0.7 on 2024-07-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OldStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('whatsapp', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('date_admission', models.DateField()),
                ('date_left', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
                ('is_qualification', models.CharField(max_length=100)),
                ('member_id', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
                ('place_holding', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
