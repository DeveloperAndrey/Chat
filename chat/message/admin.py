from django.contrib import admin
from .models import FeedbackSession, Feedback

# Модель FeedbackSession
class FeedbackSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_email', 'created_at')
    search_fields = ('user_name', 'user_email')
    list_filter = ('created_at',)

# Модель Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'specialist', 'created_at', 'message')
    search_fields = ('message', 'response', 'session__user_name')
    list_filter = ('created_at', 'specialist')

# Регистрируем модели с админскими классами
admin.site.register(FeedbackSession, FeedbackSessionAdmin)
admin.site.register(Feedback, FeedbackAdmin)