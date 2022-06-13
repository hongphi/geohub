from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from geohub.users.api.views import UserViewSet
from geohub.services.api.urls import urlpatterns

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls + urlpatterns
