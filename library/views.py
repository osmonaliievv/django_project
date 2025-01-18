from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic


# todo --------------- SEARCH ----------------
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


# todo ------------------- BOOK_LIST --------------------
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def book_list(request):
#     if request.method == 'GET':
#         book_list = models.Books.objects.all().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request, template_name='book.html', context=context)

# todo ------------------- BOOK_DETAIL --------------------
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)


# def book_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)

# todo --------------------------------------------------
def about_me(request):
    if request.method == "GET":
        return HttpResponse(
            """
            <div style='width: 400px; height: 500px; background: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; display: flex; flex-direction: column; text-align: center; margin: auto; font-family: Arial, sans-serif; background-color: #f4f4f9;'>
                <img src='https://i.pinimg.com/736x/55/0f/49/550f49a459548599a5a4ea1c67fc0244.jpg' alt='Profile Picture' style='width: 100%; height: 70%;'>
                <div style='padding: 20px;'>
                    <h2 style='margin: 0; font-size: 1.5em; color: #333;'>Осмоналиев Адилнур</h2>
                    <p style='margin: 10px 0 0; font-size: 1em; color: #666;'>Age: 18</p>
                </div>
            </div>
            """
        )


def about_my_pets(request):
    if request.method == "GET":
        return HttpResponse(
            """
                <div style='display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #eef2f7; margin: 0;'>
                    <div style='width: 400px; background: #fff; border-radius: 10px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); overflow: hidden; text-align: center; font-family: Arial, sans-serif;'>
                        <div style='padding: 20px;'>
                            <h2 style='margin: 0; font-size: 1.5em; color: #333;'>Мое любимое животное</h2>
                            <img src='https://99px.ru/sstorage/53/2023/11/mid_354064_427782.jpg' alt='Изображение собаки' style='width: 150px; height: 150px; border-radius: 50%; margin: 20px auto; object-fit: cover;'>
                            <p style='margin: 10px 0; font-size: 1em; color: #666;'>Мое любимое животное — собака.</p>
                            <p style='margin: 10px 0; font-size: 1em; color: #666;'>Собаки — верные и дружелюбные существа.</p>
                            <p style='margin: 10px 0; font-size: 1em; color: #666;'>Они всегда готовы поддержать и подарить радость.</p>
                        </div>
                    </div>
                </div>
                """)


def current_time(request):
    if request.method == "GET":
        now = datetime.now()
        formatted_time = now.strftime("%H:%M:%S")
        return HttpResponse(
            f"""
                <div style='display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #eef2f7; margin: 0; font-family: Arial, sans-serif;'>
                        <p style='margin: 10px 0; font-size: 1.2em; color: #666;'>{formatted_time}</p>
                </div>
            """
        )
