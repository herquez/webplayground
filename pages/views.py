from typing import Any
from .models import Page
from django.views.generic import list, detail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import PageForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    """
    Mixin that verifys that user is staff
    """
    def dispatch(self, request, *args: Any, **kwargs: Any):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super().dispatch(request, *args, **kwargs)

class PageListView(list.ListView):
    model = Page

class PageDetailView(detail.DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    