# Generated by Django 4.2.3 on 2023-07-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PVP_students_test_app', '0006_remove_student_subjects_alter_subject_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='evaluation_result',
            field=models.CharField(choices=[(0, 'NOT_EVALUATED'), (1, 'PASS'), (2, 'FAIL')], default=0, max_length=10),
        ),
    ]
