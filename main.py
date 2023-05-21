from flask import Flask

app = Flask(__name__)


@app.route('/get')
def predict():
    return "jsonify(result=output)"


if __name__ == "__main__":
    app.run(debug=True)