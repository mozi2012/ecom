from  reusable_functions import random_string
from  reusable_functions import input_until_equal
def random_choice():
    #1=cooperate
    #2=betray
    bot_choice=random_string("BE","CO")
    return bot_choice

def check_opponent_info(counter,last_turn_info):
    if counter==0:
        opponents_last_choice=last_turn_info["bot2_last_choice"]
    else:
        opponents_last_choice=last_turn_info["bot1_last_choice"]
    return opponents_last_choice

def fred_man(opponent_info):
    if opponent_info=="CO":
        return "CO"


def tif_for_tat(opponent_info):
    if opponent_info=="BE":
        return "BE"
    elif opponent_info=="CO":
        return "CO"
    else:
        return "CO"
    
    
def choose_strategy(strategy,last_turn_info):
    counter=0
    bot_choices={}
    while counter<2:
        opponent_info=check_opponent_info(counter,last_turn_info)
        if strategy[counter]=="random":
            bot_choice=random_choice()
        elif strategy[counter]=="tif_for_tat":
            bot_choice=tif_for_tat(opponent_info)
        elif strategy[counter]=="fred_man":
            bot_choice=fred_man(check_opponent_info(opponent_info))    
        if counter==0:
            bot_choices["bot1_choice"]=bot_choice
        else:
            bot_choices["bot2_choice"]=bot_choice
        counter+=1    
    return bot_choices            

def prisoner_sim(strategy,turns):
    last_turn_info={"bot1_last_choice":"NULL","bot2_last_choice":"NULL"}
    bot_points={"bot1_points":0,
                "bot2_points":0}
    counter=0
    while counter<turns:
        bot_choices=choose_strategy(strategy,last_turn_info)
        #1=cooperate
        #2=betray
        print("bot_cho"+str(bot_choices))
        if bot_choices["bot1_choice"]=="CO" and bot_choices["bot2_choice"]=="CO":
            bot_points["bot1_points"]+=3
            bot_points["bot2_points"]+=3
            last_turn_info={"bot1_last_choice":"CO","bot2_last_choice":"CO"}
        elif bot_choices["bot1_choice"]=="BE" and bot_choices["bot2_choice"]=="BE": 
            bot_points["bot1_points"]+=1
            bot_points["bot2_points"]+=1
            last_turn_info={"bot1_last_choice":"BE","bot2_last_choice":"BE"}
        elif bot_choices["bot1_choice"]=="BE" and bot_choices["bot2_choice"]=="CO":
            bot_points["bot1_points"]+=5
            last_turn_info={"bot1_last_choice":"BE","bot2_last_choice":"CO"}
        else:
            bot_points["bot2_points"]+=5
            last_turn_info={"bot1_last_choice":"CO","bot2_last_choice":"BE"}
        counter+=1
    return bot_points["bot1_points"],bot_points["bot2_points"]   
print(prisoner_sim(["random","tif_for_tat"],10))