# Generated by Django 2.1.4 on 2018-12-04 23:06

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes_site', '0002_auto_20181204_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='id',
        ),
        migrations.AddField(
            model_name='superhero',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default='5c070850beecb360474c552f', primary_key=True, serialize=False),
        ),
    ]
