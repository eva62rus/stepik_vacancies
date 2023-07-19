from django.urls import path
# from stepik_vacancies.vacancies.views import *
from vacancies.views import *

urlpatterns = [
    path('', MainPageView.as_view()),
    path('vacancies', AllVacanciesView.as_view()),
    path('vacancies/cat/<str:category>', VacanciesByCatView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view())
]
