from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


# todo ---------------- CREATE ----------------

class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)


# def create_todo_view(request):
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = forms.TodoForm()
#     return render(request, template_name='todo/create_todo.html',
#                   context={'form': form})


# todo ---------------- READ ----------------

class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    model = models.TodoModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def todo_list_view(request):
#     if request.method == 'GET':
#         todo_list = models.TodoModel.objects.all().order_by("-id")
#         context = {'todo_list': todo_list}
#         return render(request, template_name='todo/todo_list.html',
#                       context=context)

class TodoDetailView(generic.DetailView):
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo_id'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)


# def todo_detail_view(request, id):
#     if request.method == 'GET':
#         todo_id = get_object_or_404(models.TodoModel, id=id)
#         context = {'todo_id': todo_id}
#         return render(request, template_name='todo/todo_detail.html',
#                       context=context)


# todo ---------------- UPDATE ----------------

class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)


# def todo_update_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = forms.TodoForm(instance=todo_id)
#     return render(request, template_name='todo/update_todo.html',
#                   context={'form': form, 'id': id})


# todo ---------------- DELETE ----------------

class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     todo_id.delete()
#     return redirect('todo_list')
