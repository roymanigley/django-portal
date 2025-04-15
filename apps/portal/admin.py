from django.contrib import admin
from .models import Page, LinkBox, HtmlBox, ImageBox

admin.site.register(Page)
admin.site.register(LinkBox)
admin.site.register(ImageBox)
admin.site.register(HtmlBox)
