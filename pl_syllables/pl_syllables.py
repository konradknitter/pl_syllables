POLISH_VOVELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y']

class WordSplitter():
    def __init__(self, word: str):
        self.word = word.lower()

    def count_sylables(self):
        number_of_syllables = 0
        for id, character in enumerate(self.word):
            if character in POLISH_VOVELS:
                if not ((id + 1) < len(self.word) and character == "i" and self.word[id+1] in POLISH_VOVELS):
                    if not ((id + 1) < len(self.word) and self.word[id+1] == "u"):
                        number_of_syllables = number_of_syllables + 1
        return number_of_syllables

    def to_syllables(self):
        """
        >> WordSplitter("słowo").to_syllables()
        ["sło", "wo"]
        """
        number_of_syllables = self.count_sylables()
        if number_of_syllables > 1:
            split_word = []
            syllable_index = 0
            syllable = ""
            id = 0
            while (id < len(self.word)):
                character = self.word[id]
                if character in POLISH_VOVELS:
                    syllable_index = syllable_index + 1
                    syllable = syllable + character

                    if (id + 1) < len(self.word):
                        if character == "i" and self.word[id + 1] in POLISH_VOVELS or character == "u":
                            id = id + 1
                            syllable = syllable + self.word[id]

                    if syllable_index == number_of_syllables:
                        if id == (len(self.word) - 1):
                            split_word.append(syllable)
                            syllable = ""
                        else:
                            for sub_id, sub_character in enumerate(self.word[id+1:]):
                                syllable = syllable + sub_character
                                syllable = ""
                                id = id + 1
                    else:
                        if (id + 2) < len(self.word) and self.word[id + 1] not in POLISH_VOVELS and self.word[id + 2] not in POLISH_VOVELS:
                            if (self.word[id+1:id+3] in ("cz", "sz", "rz", "dz", "ch", "dź", "dż") or self.word[id + 1] in ("b", "s", "ś") or self.word[id + 2] in ("ł")):
                                syllable = syllable
                                split_word.append(syllable)
                                syllable = ""
                            else:
                                if (id + 3) < len(self.word) and self.word[id+1:id+3] == "drz":
                                    syllable = syllable
                                    split_word.append(syllable)
                                    syllable = ""
                                else:
                                    syllable = syllable + self.word[id + 1]
                                    split_word.append(syllable)
                                    syllable = ""
                                    id = id + 1
                        elif id == (len(self.word) - 1):
                            split_word.append(syllable)
                            syllable = ""
                        else:
                            syllable = syllable
                            split_word.append(syllable)
                            syllable = ""
                else:
                    syllable = syllable + character
                id = id + 1
            return split_word
        elif number_of_syllables == 1:
            return [self.word]
        else:
            return []

print(WordSplitter("parapseudopodia").to_syllables())