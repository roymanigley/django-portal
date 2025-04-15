from django.urls import path

from .views import CustomLoginView, CustomLogoutView, SelectOrganizationTemplateView

urlpatterns = [
    path('login/', CustomLoginView.as_view()),
    path('logout/', CustomLogoutView.as_view()),
    path('user/organization/', SelectOrganizationTemplateView.as_view()),
]
