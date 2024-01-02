#Episode 3 - https://www.youtube.com/watch?v=T6OLDHAWjjA&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=3

print("Hello, welcome to Coffee.com!")

name = input("Your name: ")

menu = "Cold Coffee\nHot Coffe\nCream Coffee\nCold Tea\nHot Tea\nPrice: $5,00"
price = 5

print("Hello, " + name + " .Here is the menu\n" + menu)

order = input("Your order: ")
amount = input("How many do you want: ")

calc = price * int(amount)

print("Total: $" + str(calc))

print("Sounds good " + name + " your order " + order + ' ' + str(calc) + " will be ready in 3 minutes.")