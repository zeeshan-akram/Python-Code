class Point:
    def __init__(self, number, name):
        self.no = number
        self.nam = name
    def name(self):
        print("I don't know my name.")


obj = Point(34, 'zeeshan')
print(obj.name())
print(f'{obj.nam}, {obj.no}')