# Generated by Django 4.2.3 on 2023-07-21 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PVP_students_test_app', '0013_alter_student_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='marks',
        ),
    ]
