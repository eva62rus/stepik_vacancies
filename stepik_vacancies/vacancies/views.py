from django.shortcuts import render
from django.views import View


# Create your views here.

class MainPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class AllVacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html')

class VacanciesBySpecializationView(View):
    def get(self, request, specialization):
        return render(request, 'vacancies.html')
