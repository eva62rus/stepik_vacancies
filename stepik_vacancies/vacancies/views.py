from django.shortcuts import render
from django.views import View
from vacancies.models import Company, Speciality, Vacancy

class MainPageView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        return render(request, 'index.html', {'specialities': specialities})


class AllVacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html')


class VacanciesByCatView(View):
    def get(self, request, category):
        return render(request, 'vacancies.html')


class CompanyView(View):
    def get(self, request, company_id):
        return render(request, 'company.html')


class VacancyView(View):
    def get(self, request, vacancy_id):
        return render(request, 'vacancy.html')
