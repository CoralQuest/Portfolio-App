from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def project_detail(request):
    return render(request, 'project_detail.html')

def project1_view(request):
    return render(request, 'project1.html')