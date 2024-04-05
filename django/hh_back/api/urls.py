from django.urls import path
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns


# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary

urlpatterns = [
    path('companies/', company_list, name='company-list'),
    path('companies/<int:id>/', company_detail, name='company-detail'),
    path('companies/<int:id>/vacancies/', company_vacancies, name='company-vacancies'),
    path('vacancies/', vacancy_list, name='vacancy-list'),
    path('vacancies/<int:id>/', vacancy_detail, name='vacancy-detail'),
    path('vacancies/top_ten/', vacancy_top_ten, name='vacancy-top-ten'),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)