from django.urls import path
from .views import HeroesAPIView

urlpatterns = [
    path("api/v1/heroes_list/", HeroesAPIView.as_view(), name="heroes"),
]