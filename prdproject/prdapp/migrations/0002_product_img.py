# Generated by Django 4.2.3 on 2023-08-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='gfft', upload_to='pic'),
            preserve_default=False,
        ),
    ]