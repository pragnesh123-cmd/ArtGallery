# Generated by Django 3.1.4 on 2021-03-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0008_everyday_life_history_nature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art_Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
