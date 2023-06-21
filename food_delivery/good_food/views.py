from django.shortcuts import render


def projects(request):
    return render(request, 'good_food/projects.html')
