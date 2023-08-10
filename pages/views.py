from .models import Page
from django.views.generic import list, detail
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class PageListView(list.ListView):
    model = Page

class PageDetailView(detail.DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']

    success_url = reverse_lazy('pages:pages')


class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = "_update_form"

    success_url = reverse_lazy('pages:pages')