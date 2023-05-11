from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Відомі жінки'
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


class WomenByCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['posts'][0].category)
        return context


class WomenDetailed(DetailView):
    model = Women
    context_object_name = 'women'
    template_name = 'women/women_detailed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['women']
        return context


class AddWomen(CreateView):
    form_class = AddWomenForm
    template_name = 'women/add_women.html'


def about(request):
    return render(request, 'women/about.html')
