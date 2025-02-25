from django.urls import path
from .views import RegisterApiView, LoginAPIView,LoginEndAPIView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('login_end/', LoginEndAPIView.as_view()),
]
