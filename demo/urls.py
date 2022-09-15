from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('fraud',views.fraud,name='fraud'),
    path('learn',views.learn,name='learn'),
    path('vote',views.vote,name='vote'),
    path('report',views.report,name='report'),
    
    path('locate',views.locate,name='locate'),
    path('hausa',views.hausa,name='hausa'),
    path('lge',views.lge,name='lge'),
    path('ward',views.ward,name='ward'),
    path('next',views.next,name='next'),
]
