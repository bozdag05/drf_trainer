from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register("heroes", HeroesViewSet)
# print(router.urls)

urlpatterns = [
    #path("api/v1/", include(router.urls), name="heroes_list_crud")
    path("api/v1/auth-heroes/", include("rest_framework.urls")),
    path("api/v1/heroes/", HeroesAPIViewList.as_view(), name="heroes"),
    path("api/v1/heroes/<int:pk>/", HeroesAPIViewUpdate.as_view(), name="hero_update"),
    path("api/v1/hero_delete/<int:pk>/", HeroesAPIViewDestroy.as_view(), name="hero_destroy"),
]