# Generated by Django 3.2.5 on 2021-07-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_course_id_teacher_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='school.Course'),
        ),
    ]