# Generated by Django 4.2.17 on 2025-01-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_choices_choices_choice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=255)),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_to', to='App.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('responder_email', models.CharField(blank=True, max_length=255, null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='App.form')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
