from django.shortcuts import render
from calculator_project.settings import BASE_DIR

def calculator_view(request):
    if request.method == 'POST':
        try:
            num1 = int(request.POST['num1'])
            num2 = int(request.POST['num2'])
            operation = request.POST['operation']
        except ValueError:
            return render(request, BASE_DIR/'calculator/templates/calculator.html', {'result': 0})

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2

        return render(request, BASE_DIR/'calculator/templates/calculator.html', {'result': result})

    return render(request, BASE_DIR/'calculator/templates/calculator.html')
