#Episode 10 - https://www.youtube.com/watch?v=fR_D_KIAYrE&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=10

#Differences between LISTs and TUPLEs

#A list is mutable and slower tha a tuple
alist = ["Bernard", "Hackwell", 92]
alist[0] = "Chuck"

print(alist)

#A tuple is immutable and faster than a list
atuple = ("Bernard", "Hackwell", 92)
atuple[0] = "Chuck"

print(atuple)