from django.urls import path

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [


    path('SilosDataIrt/',views.SilosDataIrtTable.as_view()),
    path('SilosDataIrt/<str:pk>',views.SilosDataIrtUpdateDel.as_view()),
    path('LoginEmail/',views.LoginEmailTable.as_view()),
    path('LoginEmail/<str:pk>',views.LoginEmailUpdateDel.as_view()),
    path('LoginPermissions/',views.LoginPermissionsTable.as_view()),
    path('LoginPermissions/<str:pk>',views.LoginPermissionsUpdateDel.as_view()),
    path('LoginUser/',views.LoginUserTable.as_view()),
    path('LoginUser/<str:pk>',views.LoginUserUpdateDel.as_view()),
    path('SilosAvgDay/',views.SilosAvgDayTable.as_view()),
    path('SilosAvgDay/<str:pk>',views.SilosAvgDayUpdateDel.as_view()),
    path('SilosAvgWeek/',views.SilosAvgWeekTable.as_view()),
    path('SilosAvgWeek/<str:pk>',views.SilosAvgWeekUpdateDel.as_view()),
    path('SilosAvgMonth/',views.SilosAvgMonthTable.as_view()),
    path('SilosAvgMonth/<str:pk>',views.SilosAvgMonthUpdateDel.as_view()),
    path('Silos/',views.SilosTable.as_view()),
    path('Silos/<str:pk>',views.SilosUpdateDel.as_view()),
    path('SilosError/',views.SilosErrorTable.as_view()),
    path('SilosError/<str:pk>',views.SilosErrorUpdateDel.as_view()),
    path('SilosErrorCategory/',views.SilosErrorCategoryTable.as_view()),
    path('SilosErrorCategory/<int:pk>',views.SilosErrorCategoryUpdateDel.as_view()),
    path('SilosSpecs/',views.SilosSpecsTable.as_view()),
    path('SilosSpecs/<str:pk>',views.SilosSpecsUpdateDel.as_view()),
    path('Home/', views.siloscount, name='home'),
    path('Home/<str:pk>', views.silosvalue, name='home2'),
    path('Graph/', TemplateView.as_view(template_name='graphs.html'), name='graph'),
    path('Graph/<str:pk>',views.chart.as_view() name='graph2'),
]
