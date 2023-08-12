from .models import Page
from django.views.generic import list, detail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm

class PageListView(list.ListView):
    model = Page

class PageDetailView(detail.DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'
    
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    