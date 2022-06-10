from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('mentors/', views.mentors_list, name='mentors'),
    path('mentors/<int:mentor_id>', views.request_time, name='request-mentor-time'),
    path('mentors/completed/<int:request_id>', views.completed_session, name='completed-session'),
    path('mentors/incompleted/<int:request_id>', views.incompleted_session, name='incomplete-session')
]
