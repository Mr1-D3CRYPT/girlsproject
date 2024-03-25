from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('drafts/', views.draft, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

]
