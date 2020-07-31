from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SolutionCreateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feeds-home'),
    path('solution/<int:slug>', SolutionCreateView.as_view(), name='solution_form'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create&/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('givesolutions/', views.givesolution , name='feeds-givesolution'),
    path('roadmap/', views.roadmap, name='feeds-roadmap'),
    path('careers/', views.careers, name='feeds-careers'),
    path('privacy/', views.privacy, name='feeds-privacy'),
    path('terms/', views.terms, name='feeds-terms'),
    path('faq/', views.faq, name='feeds-faq'),
    path('about/', views.about, name='feeds-about'),
]
