from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, FeedbackSessionForm, ResponseForm
from .models import Feedback, FeedbackSession
from django.contrib.auth.models import User

def home_view(request):
    # Проверяем, есть ли в сессии сохранённый session_id
    session_id = request.session.get('session_id')

    if session_id:
        # Проверяем, существует ли эта сессия в базе
        if FeedbackSession.objects.filter(id=session_id).exists():
            return redirect('feedback', session_id=session_id)
        else:
            # Если сессии нет в базе, очищаем session_id
            del request.session['session_id']

    return redirect('feedback_session')

def feedback_session_view(request):
    if request.method == 'POST':
        session_form = FeedbackSessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save()
            request.session['session_id'] = session.id  # Сохраняем session_id в сессии пользователя
            return redirect('feedback', session_id=session.id)
    else:
        session_form = FeedbackSessionForm()

    sessions = FeedbackSession.objects.all().order_by('-created_at')  # Получаем все сессии, сортируем по дате

    return render(request, 'message/feedback_session.html', {'session_form': session_form, 'sessions': sessions})


def feedback_view(request, session_id):
    session = get_object_or_404(FeedbackSession, id=session_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.session = session
            feedback.save()
            return redirect('feedback', session_id=session.id)
    else:
        form = FeedbackForm()
    messages = session.messages.all()
    return render(request, 'message/feedback_form.html', {'form': form, 'messages': messages, 'session': session})

def respond_to_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.user.is_authenticated:
        specialist = request.user
    else:
        specialist = None


    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=feedback)
        if form.is_valid():
            response = form.save(commit=False)
            response.specialist = specialist
            response.save()
            return redirect('feedback', session_id=feedback.session.id)
    else:
        form = ResponseForm(instance=feedback)
    return render(request, 'message/respond_feedback.html', {'form': form, 'feedback': feedback})
