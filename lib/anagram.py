class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [element for element in word_list if self.is_anagram(element)]

    def is_anagram(self, candidate):
        return sorted(self.word) == sorted(candidate)
