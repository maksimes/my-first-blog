from django.contrib import admin
from .models import Post, Comments




class PostInline(admin.StackedInline):
    model = Comments
    extra = 0

class AdminPost(admin.ModelAdmin):
    list_display = ["title", "created_date", "author", "total_likes",]
    ordering = ["created_date"]
    inlines = [PostInline]

admin.site.register(Post, AdminPost)