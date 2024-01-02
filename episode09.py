#Episode 9 - https://www.youtube.com/watch?v=jdTwCSxNINA&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=9

supplies = ["tent", "sleeping bags", "water", "food", "knife","marshmallows", "notebook", "ethernet cable", "flash drive"]

camp_site = ["Crystal Lake", 404, 23, True]

supplies.extend(["toilet paper", "bidet"])

#Removing things from lists
#1st method
#supplies.clear() #Remove everything from the list

#2nd  method
#supplies.remove("tent") #Remove 1 item from list
#supplies.remove("sleeping bags")

#3d method
supplies.pop(0) #Use index to remove item 
supplies.pop(0)

print(supplies)