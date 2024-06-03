class MinMaxWordFinder:
    def __init__(self):
        self.text = []

    def add_sentence(self, add):
        for i in add.split():
            self.text.append((len(i), i))

    def shortest_words(self):
        l = []
        min_ = self.text[0][0]
        for i in self.text:
            if i[0] < min_:
                l = [i[1]]
                min_ = i[0]
            elif i[0] == min_:
                l.append(i[1])
        return sorted(l)

    def longest_words(self):
        l = []
        max_ = self.text[0][0]
        for i in self.text:
            if i[0] > max_:
                l = [i[1]]
                max_ = i[0]
            if i[0] == max_ and i[1] not in l:
                l.append(i[1])
        return sorted(l)
# Ваш код

finder = MinMaxWordFinder
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))