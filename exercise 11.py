class Person:
    def __init__(self, name):
        self.n = name
    def talk(self):
        print(f'Hi! I am {self.n}')


obj = Person('Zeeshan')
obj.talk()
obj1 = Person('Akram')
obj1.talk()