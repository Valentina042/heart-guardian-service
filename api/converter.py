from classes import UserInfo


def user_info_to_dict(user_info: UserInfo):
    return {
        "id": user_info.id,
        "last_name": user_info.last_name,
        "email": user_info.email,
        "age": user_info.age,
        "telephone": user_info.telephone,
        "password": user_info.password,
        "e_name":user_info.emergency_contact.name,
        "e_last_name": user_info.emergency_contact.last_name,
        "e_email": user_info.emergency_contact.email,
        "e_relation": user_info.emergency_contact.relation,
        "e_telephone": user_info.emergency_contact.telephone,
        "e_age": user_info.emergency_contact.age
    }