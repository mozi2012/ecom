import random

def simulate(strategy,turns):
    counter=0
    win=0
    while counter<turns:
        win_door=random.randint(0,2)
        door_chosen=random.randint(0,2)
        print("win door:"+str(win_door)+" door chosen:"+str(door_chosen))
        if strategy==1:
            if door_chosen==win_door:
                win+=1
        else:
            remaining_doors = [door for door in range(3) if door != door_chosen and door != win_door]
            print("remaining door"+str(remaining_doors))
            door_revailed=random.choice(list(remaining_doors))
            print("door revailed")
            remaining_doors.remove(door_revailed)
            print("remaining door"+str(remaining_doors))
            door_switch=remaining_doors[0]
            #print("door chosen:"+str(door_chosen),"door switch:"+str(door_switch),"win door:"+str(win_door), "remaining door:"+str(remaining_doors),"door set:"+str(doors_set))   
            if door_switch==win_door:
                win+=1
            print("door chosen:"+str(door_chosen),"door switch:"+str(door_switch),"win door:"+str(win_door), "remaining door:"+str(remaining_doors),"win:", door_switch==win_door)            
        counter+=1
    return win/turns        
#print("don't switch:"+str(simulate(1,5)))
print("switch:"+str(simulate(2,5)))
