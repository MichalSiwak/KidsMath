import random


class Operation:
    def __init__(self, quantity, range_from, range_to):
        self.numbers = None
        self.quantity = quantity
        self.range_from = range_from
        self.range_to = range_to
        self.all_numbers = []
        self.operations = []
        self.operator = ""

    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.randint(self.range_from, self.range_to)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers

    def get_operations(self):
        for numbers in self.all_numbers:
            operation = self.operator.join(str(i) for i in numbers)
            operation += ' ='
            self.operations.append(operation)
        return self.operations

    @staticmethod
    def add_points(results: list):
        points = 0
        for result in results:
            if result is True:
                points += 1
            elif result is False:
                points -= 1
        if points < 0:
            points = 0
        return points


class Add(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " + "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [int(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for i in number_result:
            check_result.append((i[0] == sum(i[1])))
        return check_result


class Subtraction(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " - "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [int(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = operation[0]
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers -= number
            if answer == numbers:
                check_result.append(True)
            else:
                check_result.append(False)
        return check_result


class Multiplication(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " * "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [int(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = operation[0]
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers *= number
            if answer == numbers:
                check_result.append(True)
            else:
                check_result.append(False)
        return check_result


class Division(Operation):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.randint(self.range_from, self.range_to)
                numbers.append(number)
            for numbers[0] in numbers:
                numbers[0] = numbers[0] * numbers[1]
            self.all_numbers.append(numbers)
        return self.all_numbers

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " : "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [int(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = operation[0]
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers /= number
            if answer == numbers:
                check_result.append(True)
            else:
                check_result.append(False)
        return check_result
