from django.shortcuts import render
from django.views import View
from vacancies.models import Company, Speciality, Vacancy

class MainPageView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        spec_data = []
        for spec in specialities:
            spec_data.append({
                'cnt': len(Vacancy.objects.filter(speciality=spec.id)), # type: ignore
                'spec': spec
                })  
        companies = Company.objects.all()
        comp_data = []
        for comp in companies:
            comp_data.append({
                'cnt': len(Vacancy.objects.filter(company=comp.id)),
                'comp': comp
            })
        return render(request, 'index.html', {'specialities_data': spec_data, 'companies_data': comp_data})


class AllVacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', {'vacancies_data': vacancies, 'title': 'Все вакансии'})


class VacanciesByCatView(View):
    def get(self, request, category):
        return render(request, 'vacancies.html')


class CompanyView(View):
    def get(self, request, company_id):
        return render(request, 'company.html')


class VacancyView(View):
    def get(self, request, vacancy_id):
        return render(request, 'vacancy.html')
