from django.urls import path
from .views import HeroesAPIViewList, HeroesAPIViewUpdate, HeroesAPIViewCRUD

urlpatterns = [
    path("api/v1/heroes_list/", HeroesAPIViewList.as_view(), name="heroes"),
    path("api/v1/hero/<int:pk>/", HeroesAPIViewUpdate.as_view(), name="hero"),
    path("api/v1/hero_crud/<int:pk>/", HeroesAPIViewCRUD.as_view(), name='hero_crud')
]