"""To check whether the parentheses are syntactically valid"""


def bracket(foo1):
    count = 0
    for i in foo1:
        if i == "(":
            count += 1
        else:
            if count == 0 and i == ")":
                return print(foo1, " is Invalid")
            count -= 1

    if count == 0:
        return print(foo1, " is Valid")
    else:
        return print(foo1, " is Invalid")


bracket(")(( ))")
bracket("(()())")
bracket("(())(())")
