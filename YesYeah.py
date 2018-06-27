# Print "Yes" for number divisible by 3, "Yeah" if divisible by 5 and "YesYeah" if divisible by both

for i in range(16):
    if i % 3 == 0 and i % 5 == 0:
        print("YesYeah")
    elif i % 3 == 0:
        print("Yes")
    elif i % 5 == 0:
        print("Yeah")
    else:
        print(i)
