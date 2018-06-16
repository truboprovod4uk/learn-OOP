class Person():
    def set(self, name, age, weight, profession):
        self.name = name
        self.age = age
        self.weight = weight
        self.profession = profession

rost = Person()
rost.set('Rostyk',35,65,'engineer')


ivan = Person()
ivan.set('Ivan',19,59,'student')

print(rost.name, rost.age)