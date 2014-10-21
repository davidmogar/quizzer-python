from quizzer.domain.grade import Grade

__author__ = 'David Moreno García'


class Assessment:
    def __init__(self):
        self._questions = dict()
        self._answers = dict()
        self._grades = dict()

    def calculate_grades(self):
        self._grades = dict()

        for student_id in self._answers:
            self._grades[student_id] = Grade(student_id, self.calculate_student_grade(student_id))

    def calculate_student_grade(self, student_id):
        grade = 0

        if student_id in self._answers:
            for answer in self._answers[student_id]:
                question_id = answer.question_id
                if question_id in self._questions:
                    grade += self._questions[question_id].get_score(answer)

        return grade

    def get_statistics(self):
        statistics = dict()

        for student_id in self._answers:
            for answer in self._answers[student_id]:
                question_id = answer.question_id

                if question_id in self._questions and self._questions[question_id].get_score(answer) > 0:
                    if question_id in statistics:
                        statistics[question_id] += 1
                    else:
                        statistics[question_id] = 1

        return statistics


    def validate_grade(self, grade):
        valid = False

        if grade:
            valid = grade.grade == self.calculate_student_grade(grade.student_id)

        return valid

    def validate_grades(self):
        valid = True

        for student_id, grade in self._grades.items():
            valid = self.validate_grade(grade)
            if not valid:
                break

        return valid
