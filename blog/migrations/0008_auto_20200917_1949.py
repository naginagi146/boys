# Generated by Django 3.1.1 on 2020-09-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200917_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='media/', verbose_name='添付画像'),
        ),
    ]