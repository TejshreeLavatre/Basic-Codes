# a = int(input("Specify value of number n: "))
# if a % 2 != 0:
#     print("Weird")
# elif a % 2 == 0 and 2 <= a < 6:
#     print("Not Weird")
# elif a % 2 == 0 and 6 <= a < 21:
#     print("Weird")
# elif a % 2 == 0 and 20 < a <= 100:
#     print("Not Weird")


def select_interval():
    while True:
        for element in name:
            name_short = name.split()
            timestamp.append(name_short[2][14:23])
            print(timestamp)


name = input(print("Please enter your full name: "))
whole_num = []
for i in timestamp:
    if (i[14:19]) == "00:00":
        whole_num.append(i)
        print(whole_num)


select_interval()

   # "4771 10.182.189.79 [04/Sept/2016:23:32:09 +0000] /n 3603 81.73.150.239 [04/Sep/2016:00:05:32 +0000]"
    # name_short = name.split()
    # print(name_short)
    # print(name_short[2][14:23])
    # print(len(name_short[2]))
    # # if len(name_short) <= 2:
    #     print(name)
    # else:
    #     i = 1
    #     while i < len(name_short) - 1:
    #         a = name_short[i][0]
    #         name_short[i] = a + "."
    #         i += 1
    # print(" ".join(name_short))



#Error :killed script. Details: exceeded resource limits.
