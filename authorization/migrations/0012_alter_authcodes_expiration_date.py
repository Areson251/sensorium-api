# Generated by Django 4.2.7 on 2023-12-06 13:47

import authorization.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_alter_authcodes_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authcodes',
            name='expiration_date',
            field=models.DateTimeField(default=authorization.models.day_after),
        ),
    ]