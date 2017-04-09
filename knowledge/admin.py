from django.contrib import admin

# Register your models here.
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Document, Category, DocumentAssess, Comment, Subscribe,ReadTrace, DocumentStatus


class DocumentAdmin(admin.ModelAdmin):
    list_filter = ['name', 'author', 'category']
    search_fields = ['name', 'author', 'category']

#admin.site.register(Document, DocumentAdmin)
#admin.site.register(Document)
admin.site.register(Category)
admin.site.register(DocumentAssess)
admin.site.register(Comment)
admin.site.register(Subscribe)
admin.site.register(ReadTrace)
admin.site.register(Document, MarkdownxModelAdmin)
admin.site.register(DocumentStatus)


