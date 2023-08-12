from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'core/home.html'

class Sample(TemplateView):
    template_name = 'core/sample.html'