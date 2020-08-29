number_of_info = int(input('how many information do you want enter: '))
count = 0
user_info = {}
while count <number_of_info:
    title = input('Enter title of info: ')
    information = input('Enter info now: ')
    if title not in user_info:
        user_info[title] = information
        count += 1
    else:
        print("it already stored enter another one")
print(user_info)
print('Data Stored')