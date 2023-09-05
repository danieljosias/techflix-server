from rest_framework import generics
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.authentication import TokenAuthentication


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    lookup_url_kwarg = 'movie_id'