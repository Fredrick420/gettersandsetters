class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

def getUsername(self):
    return self.username

class Student(User):
    pass
newUser = Student("Fredrick", "mugwanjafred@gmail.com", "23414543254")

print(newUser.username)


class Animals:
    def __init__(self, moving, eating):
        self.moving = moving
        self.eating = eating

def getMoving(self):
    return self.moving
def getEating(self):
    return self.eating


class Mammals(Animals):
    pass
newAnimal = Animals("legs", "branches")

print(newAnimal.eating)










