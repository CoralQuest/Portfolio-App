from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            result = num1 + num2
        except (TypeError, ValueError):
            result = "Invalid input"
    
    return render(request, 'calculator.html', {'result': result})
