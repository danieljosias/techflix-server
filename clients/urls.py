from django.urls import path
from .views import ClientView, ClientViewDetail


urlpatterns = [
    path("clients/", ClientView.as_view()),
    path("clients/<client_id>/", ClientViewDetail.as_view())
]