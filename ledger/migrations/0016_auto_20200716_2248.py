# Generated by Django 3.0.6 on 2020-07-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0015_auto_20200712_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uid',
            field=models.CharField(default='f0cb1714c9a34e12ace51c619e1c1d59', max_length=32, unique=True),
        ),
    ]