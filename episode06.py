#Epsiode 6 - https://www.youtube.com/watch?v=nD1REhS6e3Y&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=6

print("Hello, welcome to Coffee.com!")

name = input("Your name: ")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input('Are you evil: ')
    good_deeds = input('How many good deeds have you done today: ')

    if evil_status == "yes" and int(good_deeds) < 4:
        print("You are not welcome here Evil " + name + "! GET OUT!")
        exit()
    else:
        print("So you are a good " + name + " huh. Come on in!")
else:
    print("Hello " + name + ", thank you so much for coming in today!")

menu = "Cold Coffee\nHot Coffe\nCream Coffee\nCold Tea\nHot Tea\nLatte\n"

print("Here is the MENU\n" + menu)

order = input("Your order: ")

if order == "Cold Coffee" or order == "Cold Tea":
    price = 3
elif order == "Hot Coffee" or order == "Hot Tea":
    price = 5
elif order == "Cream Coffee":
    price = 7
elif order == "Latte":
    wcream = input("Latte with Whipped Cream(yes/no): ")
    if wcream == "yes":
        price = 11
    elif wcream == "no":
        price = 10
    else:
        print("ERROR")
else:
    print("We don't have this here.")
    price = 0

amount = input("How many do you want: ")

calc = price * int(amount)

print("Total: $" + str(price))

print("Sounds good " + name + " your order " + order + ' $' + str(price) + " will be ready in 3 minutes.")