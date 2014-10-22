from quizzer.assessment import Assessment
import quizzer.deserializers.assessment_deserializer as assessment_deserializer
import quizzer.utils.url_reader as urlreader

__author__ = 'David Moreno García'


def load_assessment_from_urls(questions_url, answers_url, grades_url):
    if not questions_url or not answers_url:
        raise AttributeError("Questions and answers URLs cannot be none")

    questions_json = urlreader.read(questions_url)
    answers_json = urlreader.read(answers_url)

    grades_json = None
    if grades_url:
        grades_json = urlreader.read(grades_url)

    return create_assessment(questions_json, answers_json, grades_json)


def load_assessment_from_jsons(questions_json, answers_json, grades_json):
    if not questions_json or not answers_json:
        raise AttributeError("Questions and answers URLs cannot be none")

    return create_assessment(questions_json, answers_json, grades_json)


def create_assessment(questions_json, answers_json, grades_json):
    assessment = Assessment()

    assessment._questions = assessment_deserializer.deserialize_questions(questions_json)
    assessment._answers = assessment_deserializer.deserialize_answers(answers_json)

    if grades_json:
        assessment._grades = assessment_deserializer.deserialize_grades(grades_json)

    return assessment