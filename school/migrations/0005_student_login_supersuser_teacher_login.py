# Generated by Django 2.2.7 on 2019-12-09 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20191208_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supersuser',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Login',
            fields=[
                ('gh', models.ForeignKey(on_delete=True, primary_key=True, serialize=False, to='school.Teacher')),
                ('xm', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('yxh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Login',
            fields=[
                ('xh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='school.Stu_table')),
                ('xm', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('yxh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
    ]
