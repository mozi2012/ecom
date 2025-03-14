def input_until_less_or_greater(prompt,less_or_greater,number):
    number=int(number)
    if less_or_greater == 1:
        while True:
            returned_number=int(input(str(prompt)))
            if returned_number>number:
                print("too large")
            else:
                return returned_number
    else:
        while True:
            returned_number=int(input(str(prompt)))
            if returned_number<number:
                print("too small")
            else:
                return returned_number

def input_until_equal_except_excluded(prompt,values,*invaild_values):
    while True:
        input_value=input(str(prompt)+":")
        if input_value not in str(values):
            print("Nope. That does not exist :( ")
        elif input_value not in str(invaild_values):
            return input_value
        else:
            print(input_value+":has been excluded :( ")


def input_until_equal(prompt,*values):
        while True:
            input_value=input(str(prompt))
            if input_value not in str(values):
                print("Nope. That does not exist")
            else:
                return input_value

#def  print_dict(dict): 7


