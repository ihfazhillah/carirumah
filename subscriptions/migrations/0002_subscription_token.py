# Generated by Django 2.2.1 on 2019-06-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='token',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]