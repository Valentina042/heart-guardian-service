from classes import EmergencyContact, UserInfo
import uuid
emergency_contact = EmergencyContact("Emergency", "Contact", "emergency@example.com", "Relation", "1234567890", 30)
user_info_list = [
    UserInfo(str(uuid.uuid4()),"John", "Doe", "johndoe@example.com", 25, "9876543211", "password1", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Jane", "Smith", "janesmith@example.com", 26, "9876543212", "password2", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Michael", "Johnson", "michaeljohnson@example.com", 27, "9876543213", "password3", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Emily", "Brown", "emilybrown@example.com", 28, "9876543214", "password4", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Daniel", "Davis", "danieldavis@example.com", 29, "9876543215", "password5", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Olivia", "Miller", "oliviamiller@example.com", 30, "9876543216", "password6", emergency_contact),
    UserInfo(str(uuid.uuid4()),"David", "Wilson", "davidwilson@example.com", 31, "9876543217", "password7", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Sophia", "Taylor", "sophiataylor@example.com", 32, "9876543218", "password8", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Matthew", "Anderson", "matthewanderson@example.com", 33, "9876543219", "password9", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Emma", "Thomas", "emmathomas@example.com", 34, "9876543210", "password10", emergency_contact),
    UserInfo(str(uuid.uuid4()),"Jhon", "Baron", "jhooomn@gmail.com", 34, "9876543210", "password10", emergency_contact)
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

def update_user_by_id(user_id, new_user_info : UserInfo):
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
