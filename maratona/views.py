from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                pass
                # continuar a lógica para filtrar o email e redirecionar a url para o certificado

            except:
                response = redirect('index')
                response['Location'] += '/?error=true'
                return response

        if form.errors:
            for field_error in form.errors:
                response = redirect('skills.portfolio_register')
                response['Location'] += '?error=%s' % field_error
                return response

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = self.form_class
        context['form'] = form
        return context

