# Generated by Django 2.0.4 on 2018-04-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180422_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=10)),
                ('kidname', models.CharField(max_length=10)),
            ],
        ),
    ]
