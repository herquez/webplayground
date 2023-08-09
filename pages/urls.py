from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', views.PageDetailView.as_view(), name='page'),
]