

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def is_fat(self):
        if self.weight > 150:
            return True
        else:
            return False

    def going_to_work(self):
        print("Hey im going to work")

    def going_to_sleep(self):
        print("Hey im going to sleep")


class BodyBuilder:
    def __init__(self, name, age, height, weight, muscle_mass, fat_percentage):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.muscle_mass = muscle_mass
        self.fat_percentage = fat_percentage
        


david = Person(name='david', age=25, height=180, self.weight=85)
david.is_fat()        