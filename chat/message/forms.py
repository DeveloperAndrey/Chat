from django import forms
from .models import Feedback, FeedbackSession
from django.contrib.auth.models import User

class FeedbackSessionForm(forms.ModelForm):
    class Meta:
        model = FeedbackSession
        fields = ['user_name', 'user_email']
        labels = {
            'user_name': 'Имя пользователя',
            'user_email': 'Электронная почта',
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'Введите вашу почту для связи'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
        labels = {
            'message': 'Ваш вопрос',
        }
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Опишите ваш вопрос или проблему', 'rows': 4}),
        }

class ResponseForm(forms.ModelForm):
    specialist = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Специалист')

    class Meta:
        model = Feedback
        fields = ['response', 'specialist']  # Здесь указываются только поля модели
        labels = {
            'response': 'Ответ специалиста',
        }
        widgets = {
            'response': forms.Textarea(attrs={'placeholder': 'Введите ваш ответ на сообщение пользователя', 'rows': 4}),
        }