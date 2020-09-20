# Generated by Django 3.1.1 on 2020-09-18 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200917_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='target',
        ),
        migrations.AddField(
            model_name='post',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='添付画像'),
        ),
    ]