from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rallyapi.views import NeedViewSet, UserViewSet, DonorViewSet, DonorNeedViewSet, CommunityViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"needs", NeedViewSet, "need")
router.register(r"donor-need", DonorNeedViewSet, "donor-need")
router.register(r"community", CommunityViewSet, "community")


urlpatterns = [
    path("", include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path(
        "register", UserViewSet.as_view({"post": "register_account"}), name="register"
    ),    
    path("donors/claim/", DonorViewSet.as_view({"post": "claim"}), name="donor-claim"),
    path("needs/<int:user_id>/<int:pk>/", NeedViewSet.as_view({"get": "get_need_by_user_and_need_id"}), name="get_need_by_user_and_need_id"),
    path("needId/<int:pk>/", NeedViewSet.as_view({"get": "get_need_by_need_id"}), name="get_need_by_need_id"),
]
