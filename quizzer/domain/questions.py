from abc import ABCMeta, abstractmethod

__author__ = 'David Moreno García'


class Question(metaclass=ABCMeta):
    def __init__(self, question_id, text):
        self._question_id = question_id
        self._text = text

    @abstractmethod
    def get_score(self, answer):
        pass


class MultichoiceQuestion(Question):
    _alternatives = dict()

    def __init__(self, question_id, text):
        super().__init__(question_id, text)

    def add_alternative(self, alternative_id, text, value):
        self._alternatives[alternative_id] = self.Alternative(alternative_id, text, value)

    def get_score(self, answer):
        if answer is None:
            raise AttributeError("Answer cannot be null")

        return self._alternatives[answer.value]._value if answer.value in self._alternatives else 0

    class Alternative:
        def __init__(self, alternative_id, text, value):
            self._alternative_id = alternative_id
            self._text = text
            self._value = value


class NumericalQuestion(Question):
    correct = 0
    value_correct = 0
    value_incorrect = 0

    def __init__(self, question_id, text):
        super().__init__(question_id, text)

    def get_score(self, answer):
        if answer is None:
            raise AttributeError("Answer cannot be null")

        return self.value_correct if answer.value == self.correct else self.value_incorrect


class TrueFalseQuestion(Question):
    correct = True
    feedback = ""
    value_correct = 0
    value_incorrect = 0

    def __init__(self, question_id, text):
        super().__init__(question_id, text)

    def get_score(self, answer):
        if answer is None:
            raise AttributeError("Answer cannot be null")

        return self.value_correct if answer.value == self.correct else self.value_incorrect