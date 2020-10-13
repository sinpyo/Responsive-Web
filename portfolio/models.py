from django.db import models
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    post_notice = models.BooleanField(null=True, default=False, verbose_name="게시물 공지여부")
    post_img = models.ImageField(null=True, blank=True, verbose_name="메인 사진")
    post_title = models.CharField(max_length=50, null=False, verbose_name="게시물 제목")
    post_modifydate = models.DateTimeField(default=now, verbose_name="게시물 등록(수정)일")
    #    post_deletedate = models.DateTimeField(null=True, verbose_name="게시물 삭제일")
    post_content = RichTextUploadingField(null=False, verbose_name="게시물 내용")

    def __str__(self):
        return self.post_title
