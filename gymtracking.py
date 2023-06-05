date_list = []
weight_list = []
data = []

def input_date_and_weight_list():
    date = input("Enter date, type 'Exit' to quit: ")
    while date != "Exit":
        print(date, ' has been added to date list')
        date_list.append(date)
        date = input("Enter date, type 'Exit' to quit: ")
    
    weight = float(input("Enter weight or type '0' to quit: "))
    while weight != 0:
        print(str(weight), 'has been added to list')
        weight_list.append(weight)
        weight = float(input("Enter weight or type '0' to quit: "))
    
    update_data()

def update_data():
    global data
    data = list(zip(date_list, weight_list))

def weight_change():
    change = data[0][1] - data[-1][1]
    if change < 0:
        change = change * -1
        print("You gained", change, "lbs!")
    else:
        print("You lost ", change, " lbs!")

def system_start():
    print("WEIGHT TRACKING APP")
    name = input("To get started, please enter your name: ")
    print("Hi ", name, "!")
    print("This app offers multiple services: ")
    print("A - Enter your data")
    print("B - See your progress")
    print("X - Exit the app")

    choice = input("Please enter your selection: ")
    while choice != 'X':
        if choice == 'A':
            input_date_and_weight_list()
        elif choice == 'B':
            for date, weight in data:
                print(date, "-", weight)
        elif choice == 'C':
            weight_change()

        choice = input("Please enter your selection: ")

system_start()
