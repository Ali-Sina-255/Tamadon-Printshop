from django.urls import path

from .views import GetProfileAPIView, UpdateProfileAPIView

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("me/update-profile/", UpdateProfileAPIView.as_view(), name="update_profile"),
]
