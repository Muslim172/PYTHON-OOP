class OddEvenSeparator:
    def __init__(self):
        self.even_numbers = []
        self.odd_numbers = []
    def add_number(self, number):
        if number % 2 == 0:
            self.even_numbers.append(number)
        else:
            self.odd_numbers.append(number)
    def even(self):
        return self.even_numbers
    def odd(self):
        return self.odd_numbers
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(2)
separator.add_number(3)
separator.add_number(4)
print(separator.even())
