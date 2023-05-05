from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('ij/', views.main, name='ij'),
    path('ij/sf/', views.state1, name='sf'),
    path('ij/sp/', views.state2, name='sp'),
    path('ij/sd/', views.state3, name='sd'),
    path('ij/frameworks', views.chapterFramework, name='frameworks'),
    path('ij/programlang', views.chapterProgramLang, name='programlang'),
    path('ij/database', views.chapterDatabase, name='database'),
    path('ij/web', views.chapterWeb, name='web'),
    path('ij/teg/python', views.tegPython, name='tegPy'),
    path('ij/teg/java', views.tegJava, name='tegJa'),
    path('ij/teg/javascript', views.tegJavaScript, name='tegJaSc'),
    path('ij/teg/php', views.tegPHP, name='tegPHP'),
]