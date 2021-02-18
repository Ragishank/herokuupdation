
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fnIndex),
    path('ass1',views.assginment1),
    path('ass2/',views.assginment2,name="ass2"),
    path('ass3',views.assginment3),
    path('ass4',views.assginment4),
    path('ass5',views.assignment5),
    path('ass6',views.assignment6),
    path('ass7',views.assignment7),
    path('ass8',views.assignment8),
    path('first',views.fnFirst),
    path('second',views.fnSecond),
    path('ass9',views.assignment9),
    path('ass10',views.assignment10),
    path('ass11',views.assignment11),
    path('ass12',views.assignment12),
    path('ass13',views.assignment13),
    path('ass14',views.assignment14),
    path('ass15',views.assignment15),
    path('ass16',views.assignment16),
    path('ass17',views.assignment17),
    path('ass18',views.assignment18),
    path('ass19',views.assignment19),
    path('ass20',views.assignment20),
    path('ass21',views.assignment21),
    path('ass22',views.assignment22)
    
]
