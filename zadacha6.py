class MinMaxWordFinder:
    def __init__(self):
        self.shortest_words = []
        self.longest_words = []
    def add_sentence(self, sentence):
        words = sentence.split()
        words.sort()
        max_length = max(len(word) for word in words)
        min_length = min(len(word) for word in words)
        self.shortest_words += [word for word in words if len(word) == min_length]
        self.longest_words = list(set(self.longest_words).union(set(word for word in words if len(word) == max_length))
        self.shortest_words.sort()
        self.longest_words.sort()
    def shortest(self):
        return self.shortest_words
    def longest(self):
        return self.longest_words

finder = MinMaxWordFinder()
finder.add_sentence("The quick brown fox")
finder.add_sentence("jumps over the lazy dog")
print(finder.shortest())
print(finder.longest())
