# Generated by Django 3.1.1 on 2020-09-18 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200918_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='target',
        ),
        migrations.AddField(
            model_name='image',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='image'),
        ),
    ]
