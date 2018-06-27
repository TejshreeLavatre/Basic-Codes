# Append tuples that add upto 23 to a new list

list_0 = []
list_1 = [2, 7, 19, 8, 12, 6]
list_2 = [3, 8, 4, 9, 11, 5]
for x in list_1:
    for y in list_2:
        if x+y == 23:
            list_0.append((x, y))
print("The list of values whose sum adds upto 23 is: {}".format(list_0))
