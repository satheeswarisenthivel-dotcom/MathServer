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






