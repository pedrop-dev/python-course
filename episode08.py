#Episode 8 - https://www.youtube.com/watch?v=rW5sCgSSpI8&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=8

#Hey we're going on a camping trip! and here is the stuff we need:

#tent, sleeping bags, water, food, knife, marshmallows, notebook, ethernet cable, flash drive, toilet paper, bidet

supplies = ["tent", "sleeping bags", "water", "food", "knife","marshmallows", "notebook", "ethernet cable", "flash drive"]

camp_site = ["Crystal Lake", 404, 23, True]

#Adding items at the end of the list
#1st method - Can add 1 item per append 
#supplies.append("toilet paper")
#supplies.append("bidet")

#2nd method - Cand add more than  1 item 
#supplies.extend(["toilet paper", "bidet"])

#3d method - Not a method, just adding a list
#suplies = supplies + ["toilet paper", "bidet"]

#Adding items at any point of the list
#supplies.insert(0, "bidet")

supplies.insert[-1, "toilet paper"] #Inserting the item at the end of the list with negative number

print(supplies)