import random

for i in range(4):
    print(random.random())


for i in range(5):
    print(random.randint(10, 30))


names_for_Crs = ['Abdullah', 'Turabi', 'Saeed', 'Rafique', 'Umer']
print(random.choice(names_for_Crs))