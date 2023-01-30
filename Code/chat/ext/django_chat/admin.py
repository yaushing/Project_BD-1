from django.contrib import admin
from chat.ext.django_chat.model_admin import StatementAdmin, TagAdmin
from chat.ext.django_chat.models import Statement, Tag


admin.site.register(Statement, StatementAdmin)
admin.site.register(Tag, TagAdmin)
