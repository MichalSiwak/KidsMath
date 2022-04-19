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
        user = request.user
        is_active = user.is_active
        return render(request, 'category.html', {'form': form, 'is_active': is_active})

    def post(self, request):
        category = request.POST['category']
        amount = int(request.POST['amount'])
        range_from = int(request.POST['from'])
        range_to = int(request.POST['to'])
        if category == '5':
            return redirect('category')
        else:
            return redirect('play', category, amount, range_from, range_to)


class PlayView(View):

    def get(self, request, **kwargs):
        user = request.user
        is_active = user.is_active
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
        return render(request, 'play.html', {'operations': operations, 'is_active': is_active})

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
