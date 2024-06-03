class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, num):
        self.right += num

    def add_left(self, num):
        self.left += num

    def result(self):
        if self.left == self.right:
            return '='
        if self.left > self.right:
            return 'L'
        if self.left < self.right:
            return 'R'
# Ваш код

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())