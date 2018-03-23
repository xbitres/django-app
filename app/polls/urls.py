from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/questions/', views.QuestionsAPIView.as_view(), name="create_questions"),
    path('api/questions/<int:pk>/', views.QuestionAPIView.as_view(), name="create_questions"),
    path('api/auth', include('rest_framework.urls'), name='api_auth_web'),
    path('api/get-token', obtain_auth_token, name='api_auth_token'),
]