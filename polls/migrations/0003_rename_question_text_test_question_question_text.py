# Generated by Django 3.2 on 2021-06-23 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_text_question_question_text_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text_test',
            new_name='question_text',
        ),
    ]
