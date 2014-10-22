from flask import Flask, request, render_template
import quizzer.loaders.assessment_loader as assessment_loader
import quizzer.serializers.assessment_serializer as serializer

__author__ = 'david_000'

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:4567'


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post_form():
    questions_json = request.args.get('questions', '')
    answers_json = request.args.get('answers', '')

    if not questions_json:
        # Try to read from form
        questions_json = request.form['questions']
        answers_json = request.form['answers']

    json_grades = 'Invalid input'

    if questions_json and answers_json:
        assessment = assessment_loader.load_assessment_from_jsons(questions_json, answers_json, None)
        assessment.calculate_grades()
        json_grades = serializer.serialize_grades(assessment._grades, 'json')

    return render_template('grades.html', grades=json_grades)
