from django.urls import path
from .views import PortalView

urlpatterns = [
    path('', PortalView.as_view()),
]
