from django.shortcuts import render
from .models import BeFit


def projects(request):
    prof = BeFit.objects.all()
    context = {'profiles': prof}
    return render(request, 'good_food/projects.html', context)
