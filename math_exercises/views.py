from django.contrib.auth.mixins import LoginRequiredMixin
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
        print(numbers)
        print(operation)
        operations = operation.get_operations()
        print(operations)


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

        if category == 1:
            if typ_of_operations == 1:
                operation = Add(range_from, range_to)
            elif typ_of_operations == 2:
                operation = Subtraction(range_from, range_to)
            elif typ_of_operations == 3:
                operation = Multiplication(range_from, range_to)
            else:
                operation = Division(range_from, range_to)

        elif category == 2:
            print('zwykle')
            if typ_of_operations == 1:
                operation = FractionAdd(range_from, range_to)
            if typ_of_operations == 2:
                print('-')
            if typ_of_operations == 3:
                print('*')
            if typ_of_operations == 4:
                print('/')
        else:
            if typ_of_operations == 1:
                operation = DecimalFractionsAdd(range_from, range_to)
            if typ_of_operations == 2:
                operation = DecimalFractionsSubtraction(range_from, range_to)
            if typ_of_operations == 3:
                operation = DecimalFractionsMultiplication(range_from, range_to)
            if typ_of_operations == 4:
                operation = DecimalFractionsDivision(range_from, range_to)

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
        else:
            results = Division.checking_results(numbers, answers)
        points = Operation.add_points(results)

        kids.set_points(points)
        kids.save()
        return redirect('user')


# class DecimalFractionsView(View):
#     def get(self, request):
#         form = CategoryDecimalFractionsForm()
#         return render(request, 'decimal_fractions.html', {'form': form})
#
#     def post(self, request):
#         category = request.POST['category']
#         amount = 2
#         range_from = int(request.POST['from'])
#         range_to = int(request.POST['to'])
#         return redirect('decimal_play', category, amount, range_from, range_to)

#
# class DecimalFractionsPlayView(View):
#     def get(self, request, **kwargs):
#         category = int(kwargs['category'])
#         quantity = int(kwargs['amount'])
#         range_from = int(kwargs['range_from'])
#         range_to = int(kwargs['range_to'])
#
#         if category == 1:
#             operation = DecimalFractionsAdd(quantity, range_from, range_to)
#
#         elif category == 2:
#             operation = Subtraction(quantity, range_from, range_to)
#
#         elif category == 3:
#             operation = Multiplication(quantity, range_from, range_to)
#
#         else:
#             operation = Division(quantity, range_from, range_to)
#         # else:
#         #     print('?')
#
#         numbers = operation.draw_numbers()
#         operations = operation.get_operations()
#         cache.set('numbers', numbers)
#         return render(request, 'play.html', {'operations': operations})
#
#     def post(self, request, **kwargs):
#         category = int(kwargs['category'])
#         user = request.user.pk
#         kids = Kids.objects.get(kids_id=user)
#         numbers = cache.get('numbers')
#         answers = request.POST.getlist('results')
#         if category == 1:
#             results = Add.checking_results(numbers, answers)
#         elif category == 2:
#             results = Subtraction.checking_results(numbers, answers)
#         elif category == 3:
#             results = Multiplication.checking_results(numbers, answers)
#         else:
#             results = Division.checking_results(numbers, answers)
#         points = Operation.add_points(results)
#
#         kids.set_points(points)
#         kids.save()
#         return redirect('user')
#
#

