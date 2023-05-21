
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def questions_security():
    questions = ["¿Se está realizando alguna actividad física?", "¿Se está en reposo?","¿Presenta Mareo, Fatiga, Sudoración? "]
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
    #normal
    min_mean = statistics_data[0]-statistics_data[0]*0.10
    max_mean = min_mean = statistics_data[0]*0.10+statistics_data[0]
    if min_mean <= HR and HR<= max_mean:
        answer = "Tu ritmo cardiaco está dentro de los valores normales :)"
        return answer
    elif HR <= statistics_data[1] and HR> statistics_data[4]:
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
    elif HR>= statistics_data[3]:
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
    statistics_data = [mean_df,min_df,max_df,max_maxtolerance, min_mintolerance]
    mongo_db()
    return statistics_data

def get_data():
    file1= pd.read_excel("Datos Laura.xlsx", header=0, index_col=None)
    file2= pd.read_excel("Datos Gus.xlsx",sheet_name='5-Dic-2022', header=0, index_col=None)
    file3= pd.read_excel("Datos Gus.xlsx",sheet_name='4-Mayo', header=0, index_col=None)
    file4= pd.read_excel("Datos Gus.xlsx",sheet_name='7-Mayo', header=0, index_col=None)
    documents = [file1, file2, file3, file4]
    read_data()
    return documents