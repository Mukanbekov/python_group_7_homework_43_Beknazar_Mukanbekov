from django.shortcuts import render


def add(a, b):
    return a+b


def mul(a, b):
    return a*b


def sub(a, b):
    return a-b


def di(a, b):
    return a/b


def operation(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return sub(a, b)
    elif operator == "*":
        return mul(a, b)
    elif operator == "/":
        return di(a, b)


def calculating_numbers_views(request):
    if request.method == "GET":
        return render(request, 'calculating_numbers.html')
    elif request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        operator = request.POST.get("radio1")
        context = {
            'result': operation(a, b, operator)
                   }
        return render(request, 'calculating_numbers.html', context)
