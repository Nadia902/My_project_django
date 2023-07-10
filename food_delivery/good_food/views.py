from django.shortcuts import render
from .models import BeFit, Light, Normal, Strong, SuperStrong, Super


def projects(request):
    control = 0
    prof = BeFit.objects.all()
    prof_light = Light.objects.all()
    gender = request.GET.get('calc_gender')
    goal = request.GET.get('calc_goal')
    act = request.GET.get('calc_act')
    age = request.GET.get('calc_age')
    height = request.GET.get('calc_height')
    weight = request.GET.get('calc_weight')

    if gender == "1":
        control = round(((655.1 + (float(weight)*9.563) + (float(height)*1.85) -
                          (float(age)*4.676)) * float(act)) + float(goal))
        context = {'profiles': prof, 'control': control, 'prof_light': prof_light}
        return render(request, 'good_food/projects.html', context)
    elif gender == "2":
        control = round(((66.5 + (float(weight)*13.75) + (float(height)*5.003) -
                                  (float(age)*6.775)) * float(act)) + float(goal))
        context = {'profiles': prof, 'control': control, 'prof_light': prof_light}
        return render(request, 'good_food/projects.html', context)

    context = {'profiles': prof, 'control': control, 'prof_light': prof_light}
    return render(request, 'good_food/projects.html', context)
