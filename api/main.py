from flask import Flask, request, jsonify
from converter import user_info_to_dict
from classes import EmergencyContact, UserInfo
from service import questions_security, save_user
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


@app.route('/users/', methods=['POST'])
def sav_user():
    try:
        data = request.json['user']
        emergency_contact = EmergencyContact(
            name=data['emergencyContact']['name'],
            last_name=data['emergencyContact']['lastName'],
            email=data['emergencyContact']['email'],
            relation=data['emergencyContact']['relation'],
            telephone=data['emergencyContact']['telephone'],
            age=data['emergencyContact']['age']
        )
        user_info = UserInfo(
            id=data['id'],
            name=data['name'],
            last_name=data['lastName'],
            email=data['email'],
            age=data['age'],
            telephone=data['telephone'],
            password=data['password'],
            emergency_contact=emergency_contact
        )
        result = save_user(user_info)
        converted = user_info_to_dict(result)
        return jsonify(converted)
    except Exception as e:
        return jsonify("{}".format(str(e))), 409

if __name__ == "__main__":
    app.run(debug=True)
