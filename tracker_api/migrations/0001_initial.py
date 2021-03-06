# Generated by Django 3.0.3 on 2021-12-14 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Planning'), (2, 'Active'), (3, 'Control'), (4, 'Finished')], default=1)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('observer', models.ManyToManyField(related_name='observers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('recipients', models.ManyToManyField(related_name='recipients', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nots', to='tracker_api.Task')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.SmallIntegerField(choices=[(1, 'Planning'), (2, 'Active'), (3, 'Control'), (4, 'Finished')], default=1)),
                ('current_status', models.SmallIntegerField(choices=[(1, 'Planning'), (2, 'Active'), (3, 'Control'), (4, 'Finished')], default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_changes', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', to='tracker_api.Task')),
            ],
        ),
    ]
