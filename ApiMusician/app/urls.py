from django.urls import path
from rest_framework import urls
from app.views import MusicianListAndCreate, AlbumListAndCreate


urlpatterns = [
    path('musician/', MusicianListAndCreate.as_view()),
    path('album/', AlbumListAndCreate.as_view())
]

