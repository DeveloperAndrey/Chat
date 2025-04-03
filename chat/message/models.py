from django.db import models
from django.contrib.auth.models import User

class FeedbackSession(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сессия от {self.user_name} ({self.created_at})"

    class Meta:
        verbose_name = 'Сессия граждан'
        verbose_name_plural = 'Сессии граждан'

class Feedback(models.Model):
    session = models.ForeignKey(FeedbackSession, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    specialist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.session.user_name} ({self.created_at})"

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
