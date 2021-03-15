from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('brian', views.brian, name='brian'),   # 'brian' - the name after /hello in browser
    path('david', views.david, name='david'), 
    path('<str:name>', views.greet, name='greet') # we define after / the variable = name
]
