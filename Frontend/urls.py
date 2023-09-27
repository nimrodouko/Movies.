from django.urls import path
from Frontend import views

urlpatterns=[
    path('', views.homeview, name ='home' ),
    path('jsonpage/', views.getasjson, name='json'),
    path('download/', views.downloadpage, name ='download'),
]