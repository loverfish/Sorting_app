from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'algorithm_type', 'time_to_sort')
    list_filter = ('algorithm_type',)
    search_fields = ('title', 'algorithm_type', 'time_to_sort')
