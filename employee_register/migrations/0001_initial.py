# Generated by Django 4.0.5 on 2022-06-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vac_request', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=15)),
                ('vac_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.vacation')),
            ],
        ),
    ]
