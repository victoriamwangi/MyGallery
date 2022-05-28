# Generated by Django 4.0.4 on 2022-05-28 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=20)),
                ('location_code', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='gallery.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.location')),
            ],
        ),
    ]
