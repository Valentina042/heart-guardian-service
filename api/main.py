from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid

app = Flask(__name__)
CORS(app)


class EmergencyContact:
    def __init__(self, name, last_name, email, relation, telephone, age):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.relation = relation
        self.telephone = telephone
        self.age = age


class UserInfo:
    def __init__(self, id, name, last_name, email, age, telephone, password, emergency_contact: EmergencyContact):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.telephone = telephone
        self.password = password
        self.emergency_contact = emergency_contact


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


emergency_contact = EmergencyContact(
    "Emergency", "Contact", "emergency@example.com", "Relation", "1234567890", 30)
user_info_list = [
    UserInfo(str(uuid.uuid4()), "John", "Doe", "johndoe@example.com",
             25, "9876543211", "password1", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Jane", "Smith", "janesmith@example.com",
             26, "9876543212", "password2", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Michael", "Johnson", "michaeljohnson@example.com",
             27, "9876543213", "password3", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Emily", "Brown", "emilybrown@example.com",
             28, "9876543214", "password4", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Daniel", "Davis", "danieldavis@example.com",
             29, "9876543215", "password5", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Olivia", "Miller", "oliviamiller@example.com",
             30, "9876543216", "password6", emergency_contact),
    UserInfo(str(uuid.uuid4()), "David", "Wilson", "davidwilson@example.com",
             31, "9876543217", "password7", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Sophia", "Taylor", "sophiataylor@example.com",
             32, "9876543218", "password8", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Matthew", "Anderson", "matthewanderson@example.com",
             33, "9876543219", "password9", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Emma", "Thomas", "emmathomas@example.com",
             34, "9876543210", "password10", emergency_contact),
    UserInfo(str(uuid.uuid4()), "Jhon", "Baron", "jhooomn@gmail.com",
             34, "9876543210", "password10", emergency_contact)
]


def create_user(user_info):
    user_info.id = str(uuid.uuid4())
    user_info_list.append(user_info)
    return user_info


def read_all_users():
    return user_info_list


def read_user_by_id(user_id):
    for user_info in user_info_list:
        if user_info.id == user_id:
            return user_info
    return None


def update_user_by_id(user_id, new_user_info: UserInfo):
    for i in range(len(user_info_list)):
        if user_info_list[i].id == user_id:
            user_info_list[i] = new_user_info
            return True
    return False


def delete_user_by_id(user_id):
    for user_info in user_info_list:
        if user_info.id == user_id:
            user_info_list.remove(user_info)
            return True
    return False


def find_user_by_email(email):
    for user_info in user_info_list:
        if user_info.email == email:
            return user_info
    return None


def save_user(user):
    userFound = find_user_by_email(user.email)
    if userFound != None:
        raise Exception(
            "Ya hay un usuario con este correo registrado {}".format(user.email))
    create_user(user)
    return user


def questions_security():
    questions = ["¿Se está realizando alguna actividad física?",
                 "¿Se está en reposo?", "¿Presenta Mareo, Fatiga, Sudoración? "]
    return questions


def emergency():
    def send_email(help_contact):
        # Create a multipart message
        msg = MIMEMultipart()
        msg["From"] = help_contact[0]
        msg["To"] = help_contact[2]
        msg["Subject"] = help_contact[3]

        # Add message body
        body = MIMEText(help_contact[4], "plain")
        msg.attach(body)

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login to your email account
            server.login(help_contact[0], help_contact[1])

            # Send the email
            server.sendmail(help_contact[0], help_contact[2], msg.as_string())

            print("Email sent successfully!")
        except Exception as e:
            print("Error sending email:", str(e))
        finally:
            # Disconnect from the server
            server.quit()

    # Example usage
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"
    subject = "Hello from Python"
    message = "This is a test email sent using Python."
    send_email(help_contact)


def alert(statistics_data, HR):
    # normal
    min_mean = statistics_data[0]-statistics_data[0]*0.10
    max_mean = min_mean = statistics_data[0]*0.10+statistics_data[0]
    if min_mean <= HR and HR <= max_mean:
        answer = "Tu ritmo cardiaco está dentro de los valores normales :)"
        return answer
    elif HR <= statistics_data[1] and HR > statistics_data[4]:
        answer = "Tu ritmo cardiaco está un poco por debajo de los valores normales :/"
        questions_security()
        return answer
    elif HR >= statistics_data[2] and HR < statistics_data[3]:
        answer = "Tu ritmo cardiaco está un poco por encima de los valores normales :/"
        questions_security()
        return answer
    elif HR <= statistics_data[4]:
        answer = "Tu ritmo cardiaco está muy por debajo de los valores normales :("
        emergency()
        return answer
    elif HR >= statistics_data[3]:
        answer = "Tu ritmo cardiaco está muy por encima de los valores normales :("
        emergency()
        return answer


def mongo_db(statistics_data):
    pass


def random_HeartRate(statistics_data):
    HR = random.randint(statistics_data[1], statistics_data[2])
    return HR


def read_data(documents):
    for document in documents:
        data = pd.DataFrame(document)
        mean_df = data['BPM'].mean()
        min_df = data['BPM'].min()
        max_df = data['BPM'].max()
        max_maxtolerance = (max_df*0.15)+max_df
        min_mintolerance = min_df-(min_df*0.15)
    statistics_data = [mean_df, min_df, max_df,
                       max_maxtolerance, min_mintolerance]
    mongo_db()
    return statistics_data


def get_data():
    file1 = pd.read_excel("Datos Laura.xlsx", header=0, index_col=None)
    file2 = pd.read_excel(
        "Datos Gus.xlsx", sheet_name='5-Dic-2022', header=0, index_col=None)
    file3 = pd.read_excel(
        "Datos Gus.xlsx", sheet_name='4-Mayo', header=0, index_col=None)
    file4 = pd.read_excel(
        "Datos Gus.xlsx", sheet_name='7-Mayo', header=0, index_col=None)
    documents = [file1, file2, file3, file4]
    read_data()
    return documents


if __name__ == "__main__":
    app.run(debug=True)
