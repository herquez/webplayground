from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic import list, detail

class PageListView(list.ListView):
    template_name = 'pages/pages.html'
    model = Page

class PageDetailView(detail.DetailView):
    template_name = 'pages/page.html'
    model = Page