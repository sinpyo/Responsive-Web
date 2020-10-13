from django.contrib import admin
from portfolio.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_img', 'post_title', 'post_content', 'post_modifydate']
    list_display_links = ['post_title']
    list_per_page = 10
    #    list_filter = ['']
    search_fields = ['post_title']

    def content(self, post):
        return post.post_content[:10]