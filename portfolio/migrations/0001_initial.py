# Generated by Django 3.0.8 on 2020-10-11 19:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_notice', models.BooleanField(default=False, null=True, verbose_name='게시물 공지여부')),
                ('post_title', models.CharField(max_length=50, verbose_name='게시물 제목')),
                ('post_modifydate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='게시물 등록(수정)일')),
                ('post_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='게시물 내용')),
            ],
        ),
    ]