from django.shortcuts import render
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_calculator_view(request):
    context = {}
    if request.method == 'POST':
        dob = request.POST.get('dob')
        if dob:
            birthdate = date.fromisoformat(dob)
            age = calculate_age(birthdate)
            context['age'] = age
            context['dob'] = dob
    return render(request, 'calculator/home.html', context)
