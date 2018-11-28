'''
2 strings "s" and "t" are taken as input from user. String "t" must be a subsequence string of "s". The elements of "s"
absent in "t" are returned. Both strings must contain only alphabets and spaces. Both strings are case sensitive.
Absent elements must be returned in order of original occurence.
'''

def missingWords():
    s = input("Enter your string please: ")
    t = input("Enter your substring please: ")
    s_list = s.split(" ")
    t_list = t.split(" ")
    print("s_list: ", s_list)
    print("t_list: ", t_list)
    for entry in t_list:
        new_list = []
        for item in s_list:
            if item != entry:
                new_list.append(item)
        s_list = new_list.copy()
    print("Missing: ", new_list)


missingWords()

