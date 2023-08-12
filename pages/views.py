from typing import Any
from .models import Page
from django.views.generic import list, detail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import PageForm

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

class PageCreateView(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdateView(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'
    
class PageDeleteView(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    