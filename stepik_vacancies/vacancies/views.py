from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from vacancies.models import Company, Speciality, Vacancy
from enum import Enum


class Msg(Enum):
    SPEC_NOT_EXIST = 'В запросе передается несуществующая спициализация!'
    COMP_NOT_EXIST = 'В запросе передается несуществующая компания!'
    VAC_NOT_EXIST = 'В запросе передается несуществующая вакансия!'
    ALL_VACANCIES = "Все вакансии"
    SPEC_VACANCIES = "Вакансии по специализации "


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
        return render(request, 'vacancies.html', {'vacancies_data': vacancies, 'title': Msg.ALL_VACANCIES.value})


class VacanciesByCatView(View):
    def get(self, request, category):
        try:
            spec = Speciality.objects.get(code=category)
            vacancies = Vacancy.objects.filter(speciality=spec.id) # type:ignore
            return render(request, 'vacancies.html',
                           {'vacancies_data': vacancies, 'title': Msg.SPEC_VACANCIES.value + spec.title})
        except ObjectDoesNotExist:
            print(Msg.SPEC_NOT_EXIST.value)
 


class CompanyView(View):
    def get(self, request, company_id):
        try:
            comp = Company.objects.get(id=company_id)
            vacancies = Vacancy.objects.filter(company=comp.id) # type:ignore
            return render(request, 'company.html', {'company_data': comp, 'vacancies_data': vacancies})
        except ObjectDoesNotExist:
            print(Msg.COMP_NOT_EXIST.value)
         


class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vac = Vacancy.objects.get(id=vacancy_id)
            comp = vac.company
            return render(request, 'vacancy.html', {'vacancy_data': vac, 'company_data': comp})
        except ObjectDoesNotExist:
            print(Msg.VAC_NOT_EXIST.value)
        
