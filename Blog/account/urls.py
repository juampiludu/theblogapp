from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('register/', views.Register.as_view(), name="register"),
    path('api-token-auth/', views.CustomObtatinAuthToken.as_view(), name="api-token-auth"),
    path('profile/<int:id>/', views.UserProfile.as_view(), name="user_profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
