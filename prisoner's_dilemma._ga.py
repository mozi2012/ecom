print("your goal is to gain as manny points as posible. here are the rules: on your turn you may choose to cooperate(CO) or betray(BE). if you both CO then you both get 3 points.")
print("if only you BE than you get 5 points and the other gets nothing, but if both of you BE you both only get one point.")
algorithm_check=input("algorithms on? yes -->NO<--")
algorithm=["tif for taf",]
if algorithm_check=="yes":
    input("choose:"+str(algorithm))
max_turns=input("how many turns?")
counter=0
p1_points=0
p2_points=0
while counter<int(max_turns):
    print("p1 points "+str(p1_points))
    print("p2 points "+str(p2_points))
    p1=input("p1 cooperate(CO) or betray(BE)")
    p2=input("p2 cooperate(CO) or betray(BE)")
    print("p1:"+p1)
    print("p2:"+p2)
    if p1=="co" and p2=="co":
        p1_points+=3
        p2_points+=3
        print("you both cooperated +3")
    elif p1=="be" and p2=="be": 
         p1_points+=1
         p2_points+=1
         print("both betayed +1")
    elif p1=="be" and p2=="co":
        p1_points+=5
        print("p1 betayed p1+5 p2+0")
    else:
        p2_points+=5
        print("p2 betayed p2+5 p1+0")
    counter+=1
if p1_points>p2_points:
    print("p1 WINS")
elif p1_points<p2_points:
    print("p2 WINS")
else:
    print("tie")
print("p1 points "+str(p1_points))
print("p2 points "+str(p2_points))