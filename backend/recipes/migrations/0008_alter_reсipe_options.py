# Generated by Django 4.2.4 on 2023-09-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_reсipe_author_alter_reсipe_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reсipe',
            options={'ordering': ['id']},
        ),
    ]
