number = True
while True:
    action = input(">").lower()
    if action == 'help':
        print("""Start - To start the car. 
Stop - To Stop the car.
Quit - To Exit.""")
    elif action == 'start':
        if action == 'start' and number is True:
            print("Car Started")
            number = False
        elif action == 'start' and number is False:
            print("Car Already Started!")
    elif action == 'stop':
        if action == 'stop' and number is False:
            print("Car stop")
            number = True
        elif action == 'stop' and number is True:
            print("Car already Stop")
    elif action == 'quit':
        break
    else:
        print("I don't Understand!")