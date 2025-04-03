from django.urls import path
from .views import home_view, feedback_session_view, feedback_view, respond_to_feedback

urlpatterns = [
    path('', home_view, name='home'),  # Главная страница
    path('feedback/session/', feedback_session_view, name='feedback_session'),
    path('feedback/<int:session_id>/', feedback_view, name='feedback'),
    path('feedback/respond/<int:feedback_id>/', respond_to_feedback, name='respond_feedback'),
]