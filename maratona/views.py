from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from maratona.forms import EmailForm


class IndexView(TemplateView):
    model = None
    template_name = 'index.html'
    form_class = EmailForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = self.form_class
        context['form'] = form
        return context

