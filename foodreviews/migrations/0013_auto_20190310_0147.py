# Generated by Django 2.1.7 on 2019-03-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0012_auto_20190310_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]