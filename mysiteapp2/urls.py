
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fnIndex),
    path('ass1',views.assginment1),
    path('ass2',views.assginment2),
    path('ass3',views.assginment3)
]
