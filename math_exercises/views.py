from django.shortcuts import render, redirect
from django.views import View
from math_exercises.exercises import *
from math_exercises.forms import *


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
            task = adds.get_task()
            return render(request, 'test.html', {'task': task})
        elif category == 2:
            print('-')
        elif category == 3:
            print('*')
        elif category == 4:
            print('/')
        else:
            print('?')

        return render(request, 'test.html')

    def post(self, request, **kwargs):
        result = request.POST['result']
        print(result)
        # adds.checking_results(result)
        return redirect('category')



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
