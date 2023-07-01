from django.shortcuts import render
from .models import BeFit


def projects(request):
    prof = BeFit.objects.all()
    gender = int(request.GET.get('calc_gender'))
    goal = float(request.GET.get('calc_goal'))
    act = float(request.GET.get('calc_act'))
    age = float(request.GET.get('calc_age'))
    height = float(request.GET.get('calc_height'))
    weight = float(request.GET.get('calc_weight'))

    if gender == 1:
        control = round(((655.1 + (weight*9.563) + (height*1.85) - (age*4.676)) * act) + goal)
        context = {'profiles': prof, 'control': control}
        return render(request, 'good_food/projects.html', context)
    elif gender == 2:
        control = round(((66.5 + (weight*13.75) + (height*5.003) - (age*6.775)) * act) + goal)
        context = {'profiles': prof, 'control': control}
        return render(request, 'good_food/projects.html', context)
