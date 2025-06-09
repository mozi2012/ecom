import random
def input_until_in_range(prompt,range_tuple): 
    range_var=range(range_tuple[0],range_tuple[1])
    while True:
        try:
            input_value=int(input(str(prompt)))
            if input_value in range_var:
                return input_value
            else:
                print("That is not in the range.")
        except ValueError:
            print("That is not a number")
    


def input_until_equal_except_excluded(prompt,error_prompt,valid_values,*invalid_values):
    while True:
        counter=0
        invalid_value=False
        input_value=input(str(prompt))
        input_value=input_value.lower().replace(" ","")

        while counter<len(invalid_values):
            if input_value == invalid_values[counter].lower():
                invalid_value=True
                break
            counter+=1    

        if invalid_value==True:
            print(error_prompt)
            continue   
        
        counter=0
        while counter<len(valid_values):
            if input_value == valid_values[counter].lower():
                return input_value
            counter+=1
        print("Nope. That does not exist.")    

def input_until_equal(prompt,values):
        while True:
            input_value=input(str(prompt))
            input_value=input_value.lower().replace(" ","")
            counter=0
            while counter<len(values):
                print("input val:"+str(input_value),"val[count]:"+str(values[counter]))
                if input_value == values[counter]:
                    return input_value
                counter+=1
            print("Nope. That does not exist")

def random_string(strings):
    return str(strings[random.randint(0,len(strings)-1)])

#print(input_until_in_range("Enter a number between 1 and 10:", (1, 10)))
#print(random_string("apple", "banana", "cherry"))
#print(input_until_equal(":]","trade","yafd","poi"))
#print(input_until_equal_except_excluded(":)",":(",("trade","farm","ade","edo"),"add","ade"))
