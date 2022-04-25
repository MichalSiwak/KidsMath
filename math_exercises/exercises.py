import random
from fractions import Fraction


class Operation:
    def __init__(self, range_from, range_to):
        self.numbers = None
        self.quantity = 2
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
        answers = [float(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for i in number_result:
            check_result.append((round(i[0], 2) == sum(i[1])))
        return check_result


class Subtraction(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " - "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [float(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = round(operation[0], 2)
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers -= number
                numbers = round(numbers, 2)
            check_result.append(answer == numbers)
        return check_result


class Multiplication(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " * "

    @staticmethod
    def checking_results(numbers, answers):
        answers = [float(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = operation[0]
            answer = round(answer, 2)
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers *= number
                numbers = round(numbers, 2)
            check_result.append(answer == numbers)
        return check_result


class Division(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " : "

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

    @staticmethod
    def checking_results(numbers, answers):
        answers = [float(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            answer = round(operation[0], 2)
            numbers = operation[1][0]
            for number in operation[1][1:]:
                numbers /= number
                numbers = round(numbers, 2)
            check_result.append(answer == numbers)
        return check_result


class DecimalFractionsAdd(Add):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.uniform(self.range_from, self.range_to)
                number = round(number, 1)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers


class DecimalFractionsSubtraction(Subtraction):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.uniform(self.range_from, self.range_to)
                number = round(number, 1)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers


class DecimalFractionsMultiplication(Multiplication):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.uniform(self.range_from, self.range_to)
                number = round(number, 1)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers


class DecimalFractionsDivision(Division):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.uniform(self.range_from, self.range_to)
                number = round(number, 1)
                numbers.append(number)
            numbers[0] = round(numbers[0] * numbers[1], 2)
            self.all_numbers.append(numbers)
        return self.all_numbers


class FractionAdd(Add):
    def draw_numbers(self):
        for _ in range(5):
            for i in range(self.quantity):
                numbers = []
                denominator = random.randint(self.range_from, self.range_to)
                for _ in range(2):
                    numerator = random.randint(self.range_from, self.range_to)
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    print(fraction)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers

    @staticmethod
    def checking_results(numbers, nominator, denominator):
        decimals = list(zip(nominator, denominator))
        check_result = []
        for i in range(len(decimals)):
            if Fraction(int(decimals[i][0]), int(decimals[i][1])) == sum(numbers[i]):
                check_result.append(True)
            else:
                check_result.append(False)
        return check_result


class FractionSubtraction(Subtraction):
    def draw_numbers(self):
        for _ in range(1, 5):
            for i in range(self.quantity):
                numbers = []
                denominator = random.randint(self.range_from, self.range_to)
                for _ in range(2):
                    numerator = random.randint(self.range_from, self.range_to)
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers

    @staticmethod
    def checking_results(numbers, nominator, denominator):
        decimals = list(zip(nominator, denominator))
        print(decimals)
        check_result = []
        for i in range(len(decimals)):
            operation = numbers[i][0] - numbers[i][1]
            result = Fraction(int(decimals[i][0]), int(decimals[i][1]))
            check_result.append(operation == result)
        return check_result


class FractionMultiplication(Multiplication):
    def draw_numbers(self):
        for _ in range(1, 5):
            for i in range(self.quantity):
                numbers = []
                denominator = random.randint(self.range_from, self.range_to)
                for _ in range(2):
                    numerator = random.randint(self.range_from, self.range_to)
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers

    @staticmethod
    def checking_results(numbers, nominator, denominator):
        decimals = list(zip(nominator, denominator))
        print(decimals)
        check_result = []
        for i in range(len(decimals)):
            operation = numbers[i][0] * numbers[i][1]
            result = Fraction(int(decimals[i][0]), int(decimals[i][1]))
            check_result.append(operation == result)
        return check_result


class FractionDivision(Division):
    def draw_numbers(self):
        for _ in range(1, 5):
            for i in range(self.quantity):
                numbers = []
                denominator = random.randint(self.range_from, self.range_to)
                for _ in range(2):
                    numerator = random.randint(self.range_from, self.range_to)
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers

    @staticmethod
    def checking_results(numbers, nominator, denominator):
        decimals = list(zip(nominator, denominator))
        print(decimals)
        check_result = []
        for i in range(len(decimals)):
            operation = numbers[i][0] / numbers[i][1]
            result = Fraction(int(decimals[i][0]), int(decimals[i][1]))
            check_result.append(operation == result)
        return check_result