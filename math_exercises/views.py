from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views import View
from math_exercises.exercises import *
from math_exercises.forms import *
from sitepanel.models import Kids


class MatchTestView(View):
    def get(self, request):
        return render(request, 'test.html')

    def post(self):
        return redirect('test')


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category.html', {'form': form})

    def post(self, request):
        category = request.POST['category']
        amount = int(request.POST['amount'])
        range_from = int(request.POST['from'])
        range_to = int(request.POST['to'])
        if category == '5':
            return redirect('decimal_fractions')
        else:
            return redirect('play', category, amount, range_from, range_to)


class PlayView(View):

    def get(self, request, **kwargs):
        category = int(kwargs['category'])
        quantity = int(kwargs['amount'])
        range_from = int(kwargs['range_from'])
        range_to = int(kwargs['range_to'])

        if category == 1:
            operation = Add(quantity, range_from, range_to)

        elif category == 2:
            operation = Subtraction(quantity, range_from, range_to)

        elif category == 3:
            operation = Multiplication(quantity, range_from, range_to)

        elif category == 4:
            operation = Division(quantity, range_from, range_to)
        else:
            print('?')

        numbers = operation.draw_numbers()
        operations = operation.get_operations()
        cache.set('numbers', numbers)
        return render(request, 'play.html', {'operations': operations})

    def post(self, request, **kwargs):
        category = int(kwargs['category'])
        user = request.user.pk
        kids = Kids.objects.get(kids_id=user)
        numbers = cache.get('numbers')
        answers = request.POST.getlist('results')
        if category == 1:
            results = Add.checking_results(numbers, answers)
        elif category == 2:
            results = Subtraction.checking_results(numbers, answers)
        elif category == 3:
            results = Multiplication.checking_results(numbers, answers)
        elif category == 4:
            results = Division.checking_results(numbers, answers)
        points = Operation.add_points(results)

        kids.set_points(points)
        kids.save()
        return redirect('user')


class DecimalFractionsView(View):
    def get(self, request):
        form = CategoryDecimalFractionsForm()
        return render(request, 'decimal_fractions.html', {'form': form})

    def post(self, request):
        category = request.POST['category']
        if category == '1':
            print(category)
        elif category == '2':
            print(category)
        elif category == '3':
            print(category)
        elif category == '4':
            print(category)
        return redirect('decimal_fractions')
