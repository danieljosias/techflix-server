from django.urls import path
from .views import CommentsView, CommentsViewDetail


urlpatterns = [
    path('comments/', CommentsView.as_view()),
    path('comments/<comment_id>/', CommentsViewDetail.as_view())
]

