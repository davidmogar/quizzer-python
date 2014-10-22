from quizzer.domain.grade import Grade

__author__ = 'David Moreno García'


class Assessment:
    def __init__(self):
        self._questions = dict()
        self._answers = dict()
        self._grades = dict()

    def calculate_grades(self):
        """
        Calculate the grades of this assessment.
        """
        self._grades = dict()

        for student_id in self._answers:
            self._grades[student_id] = Grade(student_id, self.calculate_student_grade(student_id))

    def calculate_student_grade(self, student_id):
        """
        Calculates the grade of a given student.

        :param student_id: id of the student
        :return: calculated grade of the student
        """
        grade = 0

        if student_id in self._answers:
            for answer in self._answers[student_id]:
                question_id = answer.question_id
                if question_id in self._questions:
                    grade += self._questions[question_id].get_score(answer)

        return grade

    def get_statistics(self):
        """
        Returns a HashMap mapping each question id with the number of correct answers of that question.

        :return: a HashMap with the questions' statistics
        """
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
        """
        Validates the grade received as argument, checking that the value stored correspond to the grade obtained by
        the student.

        :param grade: grade to validate
        :return: true if the grade is valid, false otherwise
        """
        valid = False

        if grade:
            valid = grade.grade == self.calculate_student_grade(grade.student_id)

        return valid

    def validate_grades(self):
        """
        Validate all the grades of this assessment, checking that all the values stored in each grade correspond to
        the actual grade obtained by the students.

        :return: true if all the grades are valid, false otherwise
        """
        valid = True

        for student_id, grade in self._grades.items():
            valid = self.validate_grade(grade)
            if not valid:
                break

        return valid
