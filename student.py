import uuid

class Student:
    def __init__(self, name, password, role):
        self.id = uuid.uuid4().hex
        self.name = name
        self.password = password
        self.role = role

    def __str__(self):
        return f'id:{self.id} ' \
               f'name: {self.name}; ' \
               f'password: {self.password}; ' \
               f'role: {self.role}'