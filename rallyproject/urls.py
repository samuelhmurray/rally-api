from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rallyapi.views import NeedViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"need", NeedViewSet, "need")


urlpatterns = [
    path('', include(router.urls)),
]

