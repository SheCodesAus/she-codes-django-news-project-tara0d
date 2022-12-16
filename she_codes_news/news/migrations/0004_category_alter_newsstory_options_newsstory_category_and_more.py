# Generated by Django 4.1.3 on 2022-12-11 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_newsstory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.CharField(default='dogs', max_length=200),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
