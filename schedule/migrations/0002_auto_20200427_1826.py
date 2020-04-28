# Generated by Django 3.0.5 on 2020-04-27 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulelesson',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_lessons', to='schedule.Schedule'),
        ),
        migrations.AlterField(
            model_name='schedulelesson',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_lessons', to='schedule.Subject'),
        ),
    ]
