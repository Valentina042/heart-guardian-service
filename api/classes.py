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
