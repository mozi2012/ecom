cheese={"chedder","swiss","dr peper"}
cheese.remove("dr peper")
more_cheese={"bree"}
more_cheese.add("cottage")
both_cheese={""}
both_cheese.update(cheese,more_cheese)
both_cheese.discard("")
#print(both_cheese)
random_cheese=both_cheese.pop()
#print(both_cheese)
#print(random_cheese)
number=1
number_also=1
numbers={number,number_also}
print(numbers)