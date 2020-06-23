from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserProfileView, CustomUserView


router = DefaultRouter(trailing_slash=False)
router.register("user", CustomUserView)
router.register("user-profile", UserProfileView)


urlpatterns = [
    path("", include(router.urls))
]
