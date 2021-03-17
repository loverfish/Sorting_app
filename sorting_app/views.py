from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'sorting_app/home.html'


def index(request):
    return render(request, template_name='sorting_app/home.html')
