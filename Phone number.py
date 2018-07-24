
# def phone_number():
#     element = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     contact = input(print("Please enter a valid 10 digit contact number: "))
#     number = str(contact)
#     e164 = "+1" + number
#     try:
#         len(number) != 10 or number != element
#     except print(e164):
#         return e164
#
#
# phone_number()

def phone_number():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # print(numbers)
    contact = str(input(print("Please enter a valid 10 digit contact number: ")))
    if contact != numbers or len(contact) != 10:
        return None
    else:
        contact = str(contact)
        # contact1=contact[:3]
        # contact2=contact[3:]
        # e164 = "+1" + contact1 + "-" + contact2
        e164format = "+1" + contact
        return e164format


if __name__ == "__main__":
    number = phone_number()
    if number == None:
        print("Return value is None due to invalid input")
    else:
        print("Number in E164 format is - " + str(number))

phone_number()


# import re


# def phone_number(s):
#     pattern = re.compile("{10}")
#     return pattern.match(s)
#
#
# s = input(print("Enter valid number: "))
# if phone_number(s):
#     print("+1" + s)
# else:
#     print("Invalid Number")
#
#
# phone_number(s)
