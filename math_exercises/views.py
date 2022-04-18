from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views import View
from math_exercises.exercises import *
from math_exercises.forms import *
from sitepanel.models import Kids


class MatchTestView(View):
    def get(self, request):
        return render(request, 'test.html')

    def post(self, request):
        return redirect('test')


class CategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category.html', {'form': form})

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

    def get(self, request, *args, **kwargs):
        category = int(kwargs['category'])
        quantity = int(kwargs['amount'])
        range_from = int(kwargs['range_from'])
        range_to = int(kwargs['range_to'])

        if category == 1:
            adds = Adds(quantity, range_from, range_to)
            numbers = adds.draw_numbers()
            operations = adds.get_operations()
            cache.set('numbers', numbers)
            return render(request, 'test.html', {'operations': operations})

        elif category == 2:
            subtracts = Subtracts(quantity, range_from, range_to)
            numbers = subtracts.draw_numbers()
            operations = subtracts.get_operations()
            cache.set('numbers', numbers)
            return render(request, 'test.html', {'operations': operations})

        elif category == 3:
            multiplication = Multiplication(quantity, range_from, range_to)
            numbers = multiplication.draw_numbers()
            operations = multiplication.get_operations()
            cache.set('numbers', numbers)
            return render(request, 'test.html', {'operations': operations})

        elif category == 4:
            division = None
            numbers = None
            operations = None
            cache.set('numbers', numbers)
            return render(request, 'test.html', {'operations': operations})
        else:
            print('?')

        return render(request, 'test.html')

    def post(self, request, **kwargs):
        category = int(kwargs['category'])
        user = request.user.pk
        kids = Kids.objects.get(kids_id=user)
        numbers = cache.get('numbers')
        answers = request.POST.getlist('results')
        if category == 1:
            results = Adds.checking_results(numbers, answers)
            points = Adds.add_points(results)
        elif category == 2:
            result = Subtracts.checking_results(numbers, answers)
            points = Subtracts.add_points(result)
        elif category == 3:
            result = Multiplication.checking_results(numbers, answers)
            points = Multiplication.add_points(result)
        elif category == 4:
            pass

        kids.set_points(points)
        kids.save()

        return redirect('user')



# class PlayView(View):
#     def get(self, request, *args, **kwargs):
#         category = kwargs['category']
#         quantity = int(kwargs['amount'])
#         range_from = int(kwargs['range_from'])
#         range_to = int(kwargs['range_to'])
#         if kwargs['category'] == '1':
#             lis = Adds(quantity, range_from, range_to)
#             print(lis.draw_numbers())
#
#         elif kwargs['category'] == '2':
#             print('-')
#         elif kwargs['category'] == '3':
#             print('*')
#         elif kwargs['category'] == '4':
#             print('/')
#         else:
#             print('?')
#
#         return render(request, 'test.html')
