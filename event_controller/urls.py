from rest_framework.routers import DefaultRouter
from .views import EventMainView, EventAttenderView
from django.urls import path, include

router = DefaultRouter()
router.register("event", EventMainView)
router.register("event-attender", EventAttenderView)


urlpatterns = [
    path("", include(router.urls))
]
