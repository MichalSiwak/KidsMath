import random


class Adds:
    def __init__(self, quantity, range_from, range_to):
        self.numbers = None
        self.quantity = quantity
        self.range_from = range_from
        self.range_to = range_to

    def draw_numbers(self):
        numbers = []
        for i in range(self.quantity):
            number = random.randint(self.range_from, self.range_to)
            numbers.append(number)
        self.numbers = numbers
        return self.numbers

    def get_task(self):
        task = str(self.numbers[0])
        for i in (self.numbers[1:]):
            task += f' + {str(i)}'
        task += f' ='
        return task

    def checking_results(self, result):
        if sum(self.numbers) == result:
            return True
        else:
            return False

    def add_points(self, user):
        pass








#         self.first_number = first_number
#         self.second_number = second_number
#
#     def added(self):
#         return f'{self.first_number} + {self.second_number} = '
#
#     def subtraction(self):
#         return f'{self.first_number} - {self.second_number} = '
#
#     def added_result(self, input_result):
#         if self.first_number + self.second_number == input_result:
#             return "Dobrze"
#         else:
#             return "Źle"
#
#
# while True:
#     one = Operation(random.choice(range_of_numbers), random.choice(range_of_numbers))
#     number = int(input(one.added()))
#     print(one.added_result(number))
