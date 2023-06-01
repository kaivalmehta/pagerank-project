from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns=[
    path('about/',views.about,name='about'),
    path('demo/',views.demo,name='demo'),
    path('zero/',views.zero,name="zero"),
    path('one/',views.one,name="one"),
    path('two/',views.two,name="two"),
    path('three/',views.three,name="three"),
    path('four/',views.four,name="four"),
]
