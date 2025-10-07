# Ex.05 Design a Website for Server Side Processing
## Date:7.10.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
bmi = w/h
<br> bmi --> bmi
<br> w --> weight(in kg)
<br> h --> height(in cm)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<html> 
<head> 
<title>bmi calculator</title> 
<style>
h1 {
    border: 2px solid;
    padding: 15px;
    margin: 40px;
    border-radius: 10px;
    position: center;
    top: 200px;
    right: 1100px;
    font-size: xx-large;
    font-weight: bolder;
    font-variant: small-caps;
}

form {
    border: 5px solid rgb(13, 13, 13);
    background-color: rgb(169, 32, 54);
    padding: 30px;
    margin: 10px;
    border-radius: 20px;
    width: 425px;
    position: center;
    top: 300px;
    left: 527px;
}
</style>
</head> 
<body>
<div class="edge"> 
<div class="box"> 
<h1>bmi calculator ---S.SATHEESWARI(25017493)</h1> 
<form method="POST">
{%csrf_token %}
<div class="formelt"> 
height:<input type="text" name="height" value="{{h}}"></input>(in cm)<br/> 
</div> 
<div class="formelt"> 
weight:<input type="text" name="weight" value="{{w}}"></input>(in kg)<br/> 
</div> 
<div class="formelt"> 
<input type="submit" value="Calculate"></input><br/> 
</div> 
<div class="formelt"> 
bmi:<input type="text" name="bmi" value="{{bmi}}">
</div>
</form>
</div>
</div> 
</body>
</html>

views.py

from django.shortcuts import render 
def calculate_bmi(request): 
    context={} 
    context['bmi'] = "0" 
    context['h'] = "0" 
    context['w'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        h = request.POST.get('height','0')
        w = request.POST.get('weight','0')
        print('request=',request) 
        print('height=',h) 
        print('weight=',w) 
        bmi = int(w)/ ((int(h) / 100) ** 2) 
        context['bmi'] = bmi
        context['h'] = h
        context['w'] = w 
        print('bmi=',bmi) 
    return render(request,'mathapp/math.html',context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmicalculator/', views.calculate_bmi, name='calculate_bmi'),
    path('',views.calculate_bmi,name="bmicalculator")

]


```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (17).png>)

## HOMEPAGE:
![alt text](<Screenshot (16).png>)

## RESULT:
The program for performing server side processing is completed successfully.
