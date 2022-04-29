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
    def checking_results(numbers, answers, operator):
        answers = [None if result == '' else float(result) for result in answers]
        number_result = (list(zip(answers, numbers)))
        check_result = []
        for operation in number_result:
            if operation[0] is None:
                check_result.append(False)
            else:
                answer = round(operation[0], 2)
                numbers = operation[1][0]
                for number in operation[1][1:]:
                    if operator == 1:
                        numbers += number
                    elif operator == 2:
                        numbers -= number
                    elif operator == 3:
                        numbers *= number
                    else:
                        numbers /= number
                    numbers = round(numbers, 2)

                check_result.append(answer == numbers)
        return check_result

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


class Subtraction(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " - "


class Multiplication(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " * "


class Division(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = " : "

    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                while True:
                    number = random.randint(self.range_from, self.range_to)
                    if number == 0:
                        continue
                    numbers.append(number)
                    break

            numbers[0] = numbers[0] * numbers[1]
            self.all_numbers.append(numbers)
        return self.all_numbers


class Decimal(Operation):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                number = random.uniform(self.range_from, self.range_to)
                number = round(number, 1)
                numbers.append(number)
            self.all_numbers.append(numbers)
        return self.all_numbers


class DecimalFractionsAdd(Decimal, Add):
    pass


class DecimalFractionsSubtraction(Decimal, Subtraction):
    pass


class DecimalFractionsMultiplication(Decimal, Multiplication):
    pass


class DecimalFractionsDivision(Decimal, Division):
    def draw_numbers(self):
        for _ in range(10):
            numbers = []
            for i in range(self.quantity):
                while True:
                    number = random.uniform(self.range_from, self.range_to)
                    if round(number, 1) == 0.0:
                        continue
                    number = round(number, 1)
                    numbers.append(number)
                    break
            numbers[0] = round(numbers[0] * numbers[1], 2)
            self.all_numbers.append(numbers)
        return self.all_numbers


class Fractions(Operation):
    def draw_numbers(self):
        for _ in range(5):
            for i in range(self.quantity):
                numbers = []
                while True:
                    denominator = random.randint(self.range_from, self.range_to)
                    if denominator == 0 or denominator == 1:
                        continue
                    else:
                        break
                for _ in range(2):
                    while True:
                        numerator = random.randint(self.range_from, self.range_to)
                        if numerator == 0:
                            print(numerator)
                            continue
                        else:
                            break
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers

    @staticmethod
    def checking_results(numbers, nominator, denominator, operator):
        decimals = list(zip(nominator, denominator))
        check_result = []
        for i in range(len(decimals)):
            if decimals[i][0] == '' or decimals[i][1] == '':
                check_result.append(False)
            else:
                if operator == 1:
                    operation = numbers[i][0] + numbers[i][1]
                elif operator == 2:
                    operation = numbers[i][0] - numbers[i][1]
                elif operator == 3:
                    operation = numbers[i][0] * numbers[i][1]
                else:
                    operation = numbers[i][0] / numbers[i][1]
                result = Fraction(int(decimals[i][0]), int(decimals[i][1]))
                check_result.append(operation == result)
        return check_result


class FractionAdd(Fractions, Add):
    pass


class FractionSubtraction(Fractions, Subtraction):
    pass


class FractionMultiplication(Fractions, Multiplication):
    def draw_numbers(self):
        for _ in range(5):
            for _ in range(self.quantity):
                numbers = []
                for _ in range(2):
                    while True:
                        denominator = random.randint(self.range_from, self.range_to)
                        numerator = random.randint(self.range_from, self.range_to)
                        if denominator == 0 or numerator == 0:
                            continue
                        else:
                            break
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers


class FractionDivision(Fractions, Division):
    def draw_numbers(self):
        for _ in range(5):
            for _ in range(self.quantity):
                numbers = []
                for _ in range(2):
                    while True:
                        denominator = random.randint(self.range_from, self.range_to)
                        numerator = random.randint(self.range_from, self.range_to)
                        if denominator == 0 or numerator == 0:
                            continue
                        else:
                            break
                    fraction = Fraction(numerator, denominator, _normalize=False)
                    numbers.append(fraction)
                self.all_numbers.append(numbers)
        return self.all_numbers
