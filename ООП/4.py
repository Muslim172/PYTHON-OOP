class OddEvenSeparator:
    def __init__(self):
        self.chet = []
        self.no_chet = []

    def add_number(self, num):
        if num % 2 == 0:
            self.chet.append(num)

        else:
            self.no_chet.append(num)

    def even(self):
        return self.chet

    def odd(self):
        return self.no_chet


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
