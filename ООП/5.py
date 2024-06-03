class BigBell:
    def __init__(self):
        self.d = 2

    def sound(self):
        if self.d % 2 == 0:
            print('ding')
            self.d += 1
        else:
            print('dong')
            self.d += 1
# Ваш код

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()