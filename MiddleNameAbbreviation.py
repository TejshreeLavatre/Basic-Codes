
def select_interval():
    while True:
        for line in file large.log.txt.readlines():
        name_short = line.split()
        timestamp.append(name_short[2][14:23])
        print(timestamp)

    whole_num = []
    for i in timestamp:
        if (i[14:19]) == "00:00":
            whole_num.append(i)
    print(whole_num)
    return


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
