from django.contrib import admin
from .models import Question, Comment, Game


admin.site.register(Comment)
admin.site.register(Game)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_tags']

    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())
