from flask import Flask, request

from app import Parser

app = Flask(__name__)
# Pour lancer l'app : export FLASK_APP=hello + flask run


@app.route("/question", methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return "Désolé, cette route n'est pas faite pour être GET."
    elif request.method == 'POST':
        question = request.form["question"]

        parser = Parser(question)
        return parser.question
    else:
        return "Cette méthode n'est pas autorisée"