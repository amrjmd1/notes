# Generated by Django 2.0.1 on 2018-01-26 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('note', '0002_auto_20180123_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.User')),
            ],
        ),
    ]
