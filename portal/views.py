from django.views.generic import TemplateView
from .models import Page


class PortalView(TemplateView):

    template_name = 'portal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_position = self.request.GET.get('page', 1)

        page = Page.objects.filter(
            position=page_position
        ).prefetch_related(
            'boxes'
        ).first()
        context['page'] = page
        return context
