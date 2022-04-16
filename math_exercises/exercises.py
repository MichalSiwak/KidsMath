import random


class Adds:
    def __init__(self, quantity, range_from, range_to):
        self.numbers = None
        self.quantity = quantity
        self.range_from = range_from
        self.range_to = range_to
        self.all_numbers = []
        self.operations = []

    def draw_numbers(self):
        # for _ in range(10):
        for _ in range(2):
            numbers = []
            for i in range(self.quantity):
                number = random.randint(self.range_from, self.range_to)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers

    def get_operations(self):
        for numbers in self.all_numbers:
            operation = " + ".join(str(i) for i in numbers)
            operation += ' ='
            self.operations.append(operation)
        return self.operations

    # def checking_results(self, result):
    #     if sum(self.numbers) == result:
    #         return True
    #     else:
    #         return False

    @staticmethod
    def checking_results(numbers, results):
        results = [int(result) for result in results]
        number_result = (list(zip(results, numbers)))
        check_result = []
        for i in number_result:
            check_result.append((i[0] == sum(i[1])))
        return check_result

    @staticmethod
    def add_points(results):
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
