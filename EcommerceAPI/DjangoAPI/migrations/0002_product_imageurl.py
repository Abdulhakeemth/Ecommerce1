# Generated by Django 4.0.5 on 2022-06-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.URLField(default='aa'),
            preserve_default=False,
        ),
    ]