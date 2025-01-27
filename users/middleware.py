from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ExperienceMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = request.POST.get('experience')
            if experience:
                experience = int(experience)
                if 1 <= experience <= 3:
                    return HttpResponseBadRequest('Ваша зарплата составляет 1000$')
                elif 3 < experience <= 7:
                    return HttpResponseBadRequest('Ваша зарплата составляет 2000$')
                elif 7 < experience <= 10:
                    return HttpResponseBadRequest('Ваша зарплата составляет 5000$')
                elif experience <= 0:
                    return HttpResponseBadRequest('Ваш опыт работы не соответствует требованиям')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Зарплата не указана')
