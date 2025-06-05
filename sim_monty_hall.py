import random
def simulate(strategy,turns):
    counter=0
    win=0
    while counter<turns:
        doors=["win","nothing","nothing"]
        if strategy==1:
            if random.choice(doors)=="win":
                win+=1
        else:
            picked_door=random.choice(doors)
            doors.remove(picked_door)
            doors.remove("nothing")
            if random.choice(doors)=="win":
                win+=1
        counter+=1        
    return win/turns
print("don't switch"+str(simulate(1,10000)))
print("switch:"+str(simulate(2,10000)))           