from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rallyapi.views import NeedViewSet, UserViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"needs", NeedViewSet, "need")

urlpatterns = [
    path("", include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path(
        "register", UserViewSet.as_view({"post": "register_account"}), name="register"
    ),    
    path('needs/<int:user_id>/', NeedViewSet.as_view({'get': 'retrieve'}), name='user-needs'),

]
