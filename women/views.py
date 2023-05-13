from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import DataMixin


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


class WomenByCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs, title=str(context['posts'][0].category))
        return dict(list(c_def.items()) + list(context.items()))


class WomenDetailed(DataMixin, DetailView):
    model = Women
    context_object_name = 'women'
    template_name = 'women/women_detailed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs, title=context['women'])
        return dict(list(c_def.items()) + list(context.items()))


class AddWomen(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddWomenForm
    template_name = 'women/add_women.html'
    login_url = reverse_lazy('home')
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs, title='Додати статтю')
        return dict(list(c_def.items()) + list(context.items()))


def about(request):
    return render(request, 'women/about.html')
