# Generated by Django 4.1.7 on 2023-04-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_emp_table_comm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_table',
            name='empno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emp_table',
            name='mgr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='emp_table',
            name='sal',
            field=models.IntegerField(),
        ),
    ]
