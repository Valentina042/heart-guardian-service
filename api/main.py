from flask import Flask, request, jsonify
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


def user_info_to_dict(user_info: UserInfo):
    return {
        "id": user_info.id,
        "last_name": user_info.last_name,
        "email": user_info.email,
        "age": user_info.age,
        "telephone": user_info.telephone,
        "password": user_info.password,
        "e_name": user_info.emergency_contact.name,
        "e_last_name": user_info.emergency_contact.last_name,
        "e_email": user_info.emergency_contact.email,
        "e_relation": user_info.emergency_contact.relation,
        "e_telephone": user_info.emergency_contact.telephone,
        "e_age": user_info.emergency_contact.age
    }


if __name__ == "__main__":
    app.run(debug=True)
