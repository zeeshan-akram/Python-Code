dictionary = {
    "name" : "Zeeshan Akram",
    "email" : "email@gmail.com",
    "phone" : "12345",
    "address" : "26 area, wah cantt",
    "social media" : "I don't use social media"
}

info = input("what do you want know about me: ").lower()
if info == 'name':
    print(dictionary[info])
elif info == 'email':
    print(dictionary[info])
elif info == 'phone':
    print(dictionary[info])
elif info == 'address':
    print(dictionary[info])
elif info == 'social media':
    print(dictionary[info])
else:
    print("Sorry! i can't give you that info")