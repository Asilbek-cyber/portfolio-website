from django.urls import path,include
from .views import home_view,inner_view,portfolio_view

urlpatterns = [
    path('',home_view,name= 'home-page'),
    path('inner/',inner_view,name= 'inner-page'),
    path('portfolio/',portfolio_view,name= 'portfolio-page'),
]