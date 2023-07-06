from django.urls import path
from vacancies.views import MainPageView, AllVacanciesView, VacanciesBySpecializationView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('/vacancies', AllVacanciesView.as_view()),
    path('/vacancies/cat/')
]
