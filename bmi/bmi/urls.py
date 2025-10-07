from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmicalculator/', views.calculate_bmi, name='calculate_bmi'),
    path('',views.calculate_bmi,name="bmicalculator")

]
