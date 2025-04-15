from django.contrib.auth.views import LoginView, LogoutView, RedirectURLMixin
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView

from apps.authentication.models import User, UserOrganization


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'


class CustomLogoutView(LogoutView):
    pass


class SelectOrganizationTemplateView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponseNotAllowed(['POST'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        next = request.GET['next']
        selected_org_id = request.POST['org_id']
        has_org_relation = UserOrganization.objects.filter(
            user_id=request.user.id,
            organization_id=selected_org_id
        ).exists()
        if has_org_relation:
            User.objects.filter(
                id=request.user.id
            ).update(
                current_organization_id=selected_org_id
            )
        return HttpResponseRedirect(redirect_to=next if next else '/')
