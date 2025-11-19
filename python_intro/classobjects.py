class Employees:
    def __init__(self, name, gender, age, position):
        self.name = name
        self.gender = gender
        self.age = age
        self.position = position
employee1 = Employees('Jay Jay','Male', 21, 'Software Engineer')
employee2 = Employees('Jane Doe','Female', 25, 'Data Scientist')

print(employee1.name)
print(employee2.position)

class Developer(Employees):
        def __init__(self, name, gender, age, position, programming_language):
            super().__init__(name, gender, age, position)
            self.programming_language = programming_language
class EommissionedEmployee(Employees):
        def __init__(self, name, gender, age, position, commission_rate):
            super().__init__(name, gender, age, position)
            self.commission_rate = commission_rate
            
        pass