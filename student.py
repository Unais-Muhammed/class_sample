class Student:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    
    def set_age(self, age):
        print("You are " +str(age))

    def get_age(self, age):
        print("You are "+str(age))

    def display_student_details(self):
        print("Name : "+self.name+", "+"Age : "+self.age+ ", "+"Place : "+self.place)