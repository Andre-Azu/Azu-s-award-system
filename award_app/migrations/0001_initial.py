# Generated by Django 4.0.1 on 2022-01-11 19:36

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=1000)),
                ('average_review', models.IntegerField()),
                ('content_rating', models.ManyToManyField(related_name='rate_content', to=settings.AUTH_USER_MODEL)),
                ('design_rating', models.ManyToManyField(related_name='rate_design', to=settings.AUTH_USER_MODEL)),
                ('usability_rating', models.ManyToManyField(related_name='rate_usability', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_rate', models.IntegerField()),
                ('usability_rate', models.IntegerField()),
                ('content_rate', models.IntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_rated', to='award_app.project')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design_rated', to='award_app.project')),
                ('usability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usability_rated', to='award_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('contact', models.TextField()),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award_app.project')),
            ],
        ),
    ]
