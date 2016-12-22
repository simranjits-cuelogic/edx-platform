from .models import Reference
from django.utils import timezone

from django.views.generic import (
    ListView, FormView, UpdateView, DetailView, DeleteView
    )
from .forms import ReferenceForm

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


references_url = '/reference/references/'


class ReferenceListView(ListView):
    queryset = Reference.objects.all()
    context_object_name = 'reference_list'

    # def get_queryset(self):
    #     return self.request.user.article_set.order_by('-published_on')

class ReferenceView(FormView):
    template_name = 'reference/add.html'
    form_class = ReferenceForm
    success_url = references_url

    def form_valid(self, form):

        Reference.objects.create(
            reference_name = form.cleaned_data['reference_name'],
            reference_type = form.cleaned_data['reference_type'],
            reference_link = form.cleaned_data['reference_link'],
            reference_description = form.cleaned_data['reference_description'],
            reference_status = form.cleaned_data['reference_status'],
        )
        return super(ReferenceView, self).form_valid(form)

    def clean_reference_link(self):
        reference_link = self.cleaned_data['reference_link']
        if True:
            raise ValidationError("Reference link doesn't exist.")
        return reference_link

class ReferenceEditView(UpdateView):
    model = Reference
    template_name = 'reference/edit.html'
    form_class = ReferenceForm
    success_url = references_url

class ReferenceDetailView(DetailView):
    model = Reference
    template_name = 'reference/show.html'
    context_object_name = 'reference'

    def get_context_data(self, **kwargs):
        context = super(ReferenceDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ReferenceDeleteView(DeleteView):
    model = Reference
    success_url = references_url

    def get(self, request, *args, **kwargs):
        """ converting get request to post. Need for get_success_url action"""
        return self.post(request, *args, **kwargs)
