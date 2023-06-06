# Generated by Django 4.2.2 on 2023-06-06 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fandoms', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=21, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(editable=False, max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character1', to='works.character')),
                ('character2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character2', to='works.character')),
            ],
        ),
        migrations.CreateModel(
            name='Fanfic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('summary', models.TextField(max_length=10000)),
                ('published_date', models.DateField()),
                ('last_update_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('categories', models.ManyToManyField(to='works.categories')),
                ('characters', models.ManyToManyField(blank=True, to='works.character')),
                ('fandoms', models.ManyToManyField(blank=True, to='fandoms.fandom')),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.rating')),
                ('relashionships', models.ManyToManyField(blank=True, to='works.relationship')),
                ('tags', models.ManyToManyField(blank=True, to='works.tags')),
            ],
        ),
    ]
