from django.shortcuts import render
from .models import BeFit, Light, Normal, Strong, SuperStrong, Super
from crm.forms import OrderForm


def projects(request):
    control = 0
    prof = BeFit.objects.all()
    prof_light = Light.objects.all()
    prof_normal = Normal.objects.all()
    prof_strong = Strong.objects.all()
    prof_superstrong = SuperStrong.objects.all()
    prof_super = Super.objects.all()
    gender = request.POST.get('calc_gender')
    goal = request.POST.get('calc_goal')
    act = request.POST.get('calc_act')
    age = request.POST.get('calc_age')
    height = request.POST.get('calc_height')
    weight = request.POST.get('calc_weight')

    if gender == "1":
        control = round(((655.1 + (float(weight)*9.563) + (float(height)*1.85) -
                          (float(age)*4.676)) * float(act)) + float(goal))
    elif gender == "2":
        control = round(((66.5 + (float(weight)*13.75) + (float(height)*5.003) -
                          (float(age)*6.775)) * float(act)) + float(goal))

    context = {'profiles': prof, 'control': control, 'prof_light': prof_light,
               'prof_normal': prof_normal, 'prof_strong': prof_strong,
               'prof_superstrong': prof_superstrong, 'prof_super': prof_super}

    return render(request, 'good_food/projects.html', context)


def new_order(request):
    form = OrderForm()
    contexts = {'form': form}

    return render(request, 'good_food/neworder.html', contexts)

