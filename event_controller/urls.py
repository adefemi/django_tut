from rest_framework.routers import DefaultRouter
from .views import EventMainView
from django.urls import path, include

router = DefaultRouter()
router.register("event", EventMainView)


urlpatterns = [
    path("", include(router.urls))
]
