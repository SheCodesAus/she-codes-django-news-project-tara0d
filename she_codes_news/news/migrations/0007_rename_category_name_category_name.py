# Generated by Django 4.1.3 on 2022-12-12 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsstory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
