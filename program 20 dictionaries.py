user = {
    "name" : "Zeeshan",
    "email" : "zeeshn@gmail.com",
    "phone" : "1234"
}
print(user["name"])
print(user.get("birthday", "1998")) #get doesn't return error also can assign new attribute which are not present.
print(user.get("address", "26 area, Wah cantt"))