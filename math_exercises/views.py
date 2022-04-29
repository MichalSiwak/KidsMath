from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views import View
from math_exercises.exercises import *
from math_exercises.forms import *
from sitepanel.models import Kids


class MatchTestView(View):
    def get(self, request):
        operation = FractionAdd(1,10)
        numbers = operation.draw_numbers()
        operations = operation.get_operations()
        return render(request, 'test.html', {'operations': operations})

    def post(self):
        return redirect('test')


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category.html', {'form': form})

    def post(self, request):
        category = request.POST['category']
        operations = request.POST['operations']
        range_from = int(request.POST['from'])
        range_to = int(request.POST['to'])
        return redirect('play', category, operations, range_from, range_to)


class PlayView(View):
    def get(self, request, **kwargs):
        category = int(kwargs['category'])
        typ_of_operations = int(kwargs['operations'])
        range_from = int(kwargs['range_from'])
        range_to = int(kwargs['range_to'])
        if range_to - range_from < 9:
            print(range_to - range_from)
            messages.warning(request, 'Zbyt mały zakres')
            return redirect('category')

        if category == 1:
            operation_type = 'total'
            if typ_of_operations == 1:
                operation = Add(range_from, range_to)
            elif typ_of_operations == 2:
                operation = Subtraction(range_from, range_to)
            elif typ_of_operations == 3:
                operation = Multiplication(range_from, range_to)
            else:
                operation = Division(range_from, range_to)

        elif category == 2:
            operation_type = 'fraction'
            if typ_of_operations == 1:
                operation = FractionAdd(range_from, range_to)
            elif typ_of_operations == 2:
                operation = FractionSubtraction(range_from, range_to)
            elif typ_of_operations == 3:
                operation = FractionMultiplication(range_from, range_to)
            else:
                operation = FractionDivision(range_from, range_to)

        else:
            operation_type = 'decimal'
            if typ_of_operations == 1:
                operation = DecimalFractionsAdd(range_from, range_to)
            elif typ_of_operations == 2:
                operation = DecimalFractionsSubtraction(range_from, range_to)
            elif typ_of_operations == 3:
                operation = DecimalFractionsMultiplication(range_from, range_to)
            else:
                operation = DecimalFractionsDivision(range_from, range_to)

        numbers = operation.draw_numbers()
        operations = operation.get_operations()
        cache.set('numbers', numbers)
        return render(request, 'play.html', {'operations': operations, 'operation_type': operation_type})

    def post(self, request, **kwargs):
        category = int(kwargs['category'])
        operations = int(kwargs['operations'])
        user = request.user.pk
        kids = Kids.objects.get(kids_id=user)
        numbers = cache.get('numbers')
        answers = request.POST.getlist('results')
        numerator = request.POST.getlist('numerator')
        denominator = request.POST.getlist('denominator')
        if category == 2:
            if operations == 1:
                results = FractionAdd.checking_results(numbers, numerator, denominator)
            elif operations == 2:
                results = FractionSubtraction.checking_results(numbers, numerator, denominator)
            elif operations == 3:
                results = FractionMultiplication.checking_results(numbers, numerator, denominator)
            else:
                results = FractionDivision.checking_results(numbers, numerator, denominator)
        else:
            results = Operation.checking_results(numbers, answers, operations)

        points = Operation.add_points(results)

        kids.set_points(points)
        kids.save()
        return redirect('user')
