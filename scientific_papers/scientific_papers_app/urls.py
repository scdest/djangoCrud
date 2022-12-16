from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('tab/', views.index_tab, name='main'),
    path('papers/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.new_paper, name='new_paper'),
    path('create/', views.create, name='create'),
    path('paper/<int:id>/view/', views.paper_view, name='paper_view'),
    path('paper/<int:id>/edit/', views.paper_edit, name='paper_edit'),
    path('paper/<int:id>/delete/', views.paper_delete, name='paper_delete'),
]