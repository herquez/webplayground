from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView

class PageListView(ListView):
    template_name = 'pages/pages.html'
    model = Page

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})