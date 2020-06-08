water = 400
milk = 540
beans = 120
cups = 9
cash = 550


def inventory():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(cash, "of money")
     
     
while True:
    command = input("Write action (buy, fill, take, remaining, exit):")
    if command == "exit":
        break
    elif command == "remaining":
        inventory()
    elif command == "buy":
        order = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        if order == "back":
            continue
        elif order == "1":
            if water < 250:
                print("Sorry, not enough water!")
                continue
            elif beans < 16:
                print("Sorry, not enough beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough cups!")
                continue
            water = water - 250
            beans = beans - 16
            cups = cups - 1
            cash = cash + 4
            print("I have enough resources, making you a coffee!")
        elif order == "2":
            if water < 350:
                print("Sorry, not enough water!")
                continue
            elif milk < 75:
                print("Sorry, not enough milk!")
                continue
            elif beans < 20:
                print("Sorry, not enough beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough cups!")
                continue
            water = water - 350
            milk = milk - 75
            beans = beans - 20
            cups = cups - 1
            cash = cash + 7
            print("I have enough resources, making you a coffee!")
        elif order == "3":
            if water < 200:
                print("Sorry, not enough water!")
                continue
            elif milk < 100:
                print("Sorry, not enough milk!")
                continue
            elif beans < 12:
                print("Sorry, not enough beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough cups!")
                continue
            water = water - 200
            milk = milk - 100
            beans = beans - 12
            cups = cups - 1
            cash = cash + 6
            print("I have enough resources, making you a coffee!")
    elif command == "fill":
        fill_water = int(input("Write how many ml of water do you want to add:"))
        fill_milk = int(input("Write how many ml of milk do you want to add:"))
        fill_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        water = water + fill_water
        milk = milk + fill_milk
        beans = beans + fill_beans
        cups = cups + fill_cups
    elif command == "take":
        print("I gave you $", cash)
        cash = 0
