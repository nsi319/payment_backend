# Generated by Django 2.1.5 on 2020-02-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('rollno', models.IntegerField()),
                ('webmail', models.CharField(default='', max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transact_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('added_to_block', models.BooleanField(default=False)),
            ],
        ),
    ]
