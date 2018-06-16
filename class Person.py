#створюємо class Person
class Person():
# створюємо метод класу Person (фунція)
    def set(self, name, age, weight, profession):
        self.name = name
        self.age = age
        self.weight = weight
        self.profession = profession

#створюємо еземпляр класу Person
rost = Person()
rost.set('Rostyk',35,65,'engineer')

#ще один еземпляр класу Person
ivan = Person()
ivan.set('Ivan',42,84,'businessman')

#створюємо клас Student і наслідуємо його від Person
class Student(Person):
    def stu(self,course):
        self.course = course

#створюємо екзкмпляр класу Student
petro = Student()
petro.set('Petro',18, 58, 'student')
petro.stu(2)

print(rost.name, rost.age, petro.course)
