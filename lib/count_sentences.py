#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace ! and ? with . to standardize sentence endings
        text = self.value.replace('!', '.').replace('?', '.')
        # Split on .
        sentences = text.split('.')
        # Filter out empty strings and whitespace-only strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
