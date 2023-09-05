from rest_framework import generics
from .models import Comments
from .serializers import CommentSerializer
from rest_framework.authentication import TokenAuthentication

class CommentsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentsViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = 'comment_id'