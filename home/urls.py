
from .views import *
from django.urls import path,re_path
from .views import home, Register_in_all_table,pages,index,model_counts_view

urlpatterns = [
    path("", home, name="home"),
    path("register/", Register_in_all_table, name="register"),
    path('dashbord/', index, name='dashbord'),
    re_path("dash/", pages, name='pages'),
    re_path("model_counts_view/", model_counts_view, name='model_counts_view'),
    path("Resansman/", Resansman, name='Resansman'),
    path('model_counts/', model_counts_view, name='model_counts'),
    path('model_people/<str:model_name>/', model_people_view, name='view_people'),
    path('download_pdf/<int:person_id>/', download_pdf, name='download_pdf'),
  

]
