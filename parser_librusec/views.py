from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms
from django.views import generic


class LibrusecListView(generic.ListView):
    template_name = 'parser/mybook_list.html'
    context_object_name = 'mybook'
    model = models.LibrusecParser

    def get_queryset(self):
        return self.model.objects.all()


class LibrusecFormView(generic.FormView):
    template_name = 'parser/mybook_form.html'
    form_class = forms.BookForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг успешно завершен')
        else:
            return super(LibrusecFormView, self).post(request, *args, **kwargs)
