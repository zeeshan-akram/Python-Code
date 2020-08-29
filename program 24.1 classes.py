class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


obj = Point()
obj.x = 10;
print(obj.x)
print(obj.draw())

obj2 = Point()
obj2.x = 1
print(obj2.x)
print(obj2.move())
