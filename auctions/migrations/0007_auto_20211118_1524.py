# Generated by Django 3.2.8 on 2021-11-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auction_listing_initial_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='image_link',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
