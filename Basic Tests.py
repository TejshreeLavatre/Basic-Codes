# Transposing a dictionary

food = {"milk": "white", "carrots": "orange", "lemon": "yellow", "grapes": "purple"}
print(food)
food_transpose = {food[key]: key for key in food}
print(food_transpose)

#Defining and using a function

"""When we specify a value for the function to return, and use the command print(function), it returns the value specified. Else, it returns None"""

def new_food(any):
    variable = print("\nInput was: {}\n".format(any))
    abc = "sea cod capsules\n"
    return abc


print(new_food("yeah"))


def new_food2(any):
    variable = print("\nFood 2 input was: {}\n".format(any))
    abc = "sea cod capsules"


print(new_food2("yeah"))
