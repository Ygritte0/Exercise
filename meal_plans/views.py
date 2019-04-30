from django.shortcuts import render

# Create your views here.
def index(request):
    """膳食规划的笔记"""
    return render(request, 'meal_plans/index.html')