from flask import Flask, jsonify
from api.service import questions_security
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get')
def predict():
    return "jsonify(result=output)"

@app.route('/questions')
def questions_list():
    questions = questions_security()
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)