from django.contrib import admin

from .models import Article, Comment

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    # Show more information about the articles.
    list_display = ["title", "author", "created_date"]

    # Add link to selected attributes for reaching the content.
    list_display_links = ["title", "created_date"]

    # Add search field for stated attributes.
    search_fields = ["title"]

    # Add filter for stated attributes.
    list_filter = ["created_date", "author"]

    # Bound ArticleAdmin and Article, the name have to be 'Meta'.
    class Meta:
        model = Article


admin.site.register(Comment)
