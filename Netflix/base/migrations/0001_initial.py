# Generated by Django 4.0.5 on 2022-10-11 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=20)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(upload_to='movies')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cast', models.TextField(max_length='max', null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Experimental', 'Experimental'), ('Fantasy', 'Fantasy'), ('Historical', 'Historical'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Western', 'Western')], max_length=20)),
                ('poster', models.ImageField(upload_to='flyers')),
                ('age', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=10)),
                ('videos', models.ManyToManyField(to='base.video')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('profiles', models.ManyToManyField(blank=True, to='base.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
