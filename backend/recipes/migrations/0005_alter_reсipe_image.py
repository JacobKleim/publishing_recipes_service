# Generated by Django 4.2.4 on 2023-09-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_reсipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reсipe',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='recipes/images/'),
        ),
    ]
