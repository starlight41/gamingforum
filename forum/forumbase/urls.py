from django.urls import path
from . import views
from forumusers import views as user_view 


app_name = 'forumbase'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    # CRUD Function
    path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="question-create"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="question-detail"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="question-update"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name="question-delete"),
    path('questions/<int:pk>/comment/', views.AddCommentView.as_view(), name="question-comment"),
    path('like/<int:pk>', views.like_view, name="like_post"),
    path('profile/', user_view.profile, name="profile"),

    #tags
    path('question-taglists/', views.QuestionListAPIView.as_view(), name="question-taglists"),
]
