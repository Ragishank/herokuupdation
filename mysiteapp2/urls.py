
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
    path('second',views.fnSecond)
    
]
