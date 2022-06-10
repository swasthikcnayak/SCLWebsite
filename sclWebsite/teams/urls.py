from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_team, name='teams'),
    path('<int:team_id>/', views.single_team, name='team')
]
