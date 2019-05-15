# Transposing a dictionary

food = {"milk": "white", "carrots": "orange", "lemon": "yellow", "grapes": "purple"}
print(food)
food_transpose = {food[key]: key for key in food}
print(food_transpose)
