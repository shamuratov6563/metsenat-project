# Generated by Django 5.1.4 on 2025-01-11 14:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.RemoveField(
            model_name='books',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='recommendedby',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='users/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(null=True, upload_to='posters/')),
                ('caption', models.TextField(null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='orm.user')),
                ('tagged_users', models.ManyToManyField(to='orm.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('gif', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.user')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_reply', to='orm.comment')),
                ('top_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_top', to='orm.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='contents/')),
                ('order', models.IntegerField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.post')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='orm.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_like', to='orm.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follower', to='orm.user')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='orm.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
