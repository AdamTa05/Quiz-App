from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.start_quiz_view, name='start'),
    path('get-questions/start', views.get_questions, {'is_start': True}, name='get-questions-start'),
    path('get-questions', views.get_questions, {'is_start': False}, name='get-questions'),
    path('get-answer', views.get_answer, name='get-answer'),
    path('get-finish', views.get_finish, name='get-finish'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]