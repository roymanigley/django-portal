from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .models import Page


class PortalView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        org_id = self.request.user.current_organization.id
        page_id = self.request.GET.get('page')
        if not page_id:
            current_page = Page.objects.get_by_org_id_with_boxes(org_id=org_id).first()
        else:
            current_page = Page.objects.get_by_id_with_boxes(id=page_id, org_id=org_id)
        if current_page is None:
            raise Http404(
                _("page not found")
            )
        page_positions = Page.objects.get_by_org_id(org_id=org_id).all()
        context['current_page'] = current_page
        context['pages'] = page_positions
        return context
