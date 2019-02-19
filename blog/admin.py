from django.contrib import admin
from .models import Post, Comments, Feedback




class PostInline(admin.StackedInline):
    model = Comments
    extra = 0

class AdminPost(admin.ModelAdmin):
    list_display = ["title", "created_date", "author", "total_likes",]
    ordering = ["created_date"]
    inlines = [PostInline]


class CommentsAdmin (admin.ModelAdmin):
    list_display = ['author', 'comments_post', 'published_date',]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['author', 'name', 'email', 'send_date']


admin.site.register(Post, AdminPost)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Feedback, FeedbackAdmin)