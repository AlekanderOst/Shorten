from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Links
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowCreatorLinksView(ListView):
    model = Links
    template_name = 'links/user_links.html'
    context_object_name = 'creator_links'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Links.objects.filter(creator=user)

    def get_context_data(self, **kwards):
        ctx = super(ShowCreatorLinksView, self).get_context_data(**kwards)
        ctx['title'] = 'Link '
        return ctx


class ShowLinksView(ListView):
    model = Links
    template_name = 'links/links.html'
    context_object_name = 'links'

    def get_context_data(self, **kwards):
        ctx = super(ShowLinksView, self).get_context_data(**kwards)
        ctx['title']='Links'
        return ctx

class Createlinks(LoginRequiredMixin, CreateView):
    model = Links
    template_name = 'links/create_links.html'

    fields = ['long', 'short']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(Createlinks, self).get_context_data(**kwards)
        ctx['title'] ='Link creation'
        ctx['btn_text'] = 'Create link '
        return ctx
