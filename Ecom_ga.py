import random
from reusable_functions import input_until_less_or_greater
from reusable_functions import input_until_equal
from reusable_functions import input_until_equal_except_excluded


def gather_settings():
    #players=input_until_less_or_greater("number of players less than six:",1,6)
    players=2
    #turns_in_month=input_until_less_or_greater("how many turns/days in each month:",2,1)
    turns_in_month=1
    #years=reset_input_until_less_or_greater("how many years. 12 months in one year:",2,1)
    years=2
    return({"years":int(years),
            "turns in month":int(turns_in_month),
            "player amount":int(players)})

settings=gather_settings()

def pro(players):
    player_save=[{},{},{},{},{}]
    counter=0
    resoures={"meat":{"deer":0},
              "vegetables":{"potato":0}}
    while counter < players:
        print("player"+str(counter+1))
        #pro=input_until_equal("choose your profession. farmer,hunter:","farmer","hunter")
        pro="farmer"
        player_save[counter]["profession"]=pro
        player_save[counter]["resoures"]=resoures
        if pro=="farmer":
            player_save[counter]["resoures"]["vegetables"]["potato"]=10
        counter+=1
    return(player_save)

player_save=pro(settings["player amount"])
print(player_save)
def trade(player_amount,current_player,player_save):
    player_amount_ls=[]
    if player_amount==1:
        print("there's no one around to trade")
        return "error"
    print("you can trade with:")
    for x in range(player_amount):
        player_amount_ls.append(x+1)
        if current_player==x:
            print("you can't trade with yourself")
        else:
            print("player:"+str(x+1))       
        player_chosen=int(input_until_equal_except_excluded("input player number: ",tuple(player_amount_ls),current_player+1))-1
        print(player_save[current_player]["resoures"])       


def next_turn(input,settings,player_save,current_player):
    while True:
        if input=="trade":
               updated_player_save=trade(settings["player amount"],current_player,player_save)
        if updated_player_save!="error":
            return updated_player_save
        


def game_loop(settings,player_save):
    months=["Mar","Apr","May","Jun","Jul","Aug","sep","Oct","Nov","Dec","Jan","Feb"]
    time={"year":1,
          "month":0,
          "day":0}
    while time["month"]<settings["years"]*12:
        counter=0
        if time["day"]==settings["turns in month"]:
            time["day"]=0
            time["month"]+=1
        if time["month"]==len(months):
            time["month"]=0
            time["year"]+=1
        while counter<settings["player amount"]:
            print("year:"+str(time["year"]))
            print("month:"+str(months[time["month"]]))
            print("day:"+str(time["day"]+1))
            print("player "+str(counter+1)+" it is your turn :)")
            if player_save[counter]["profession"]=="hunter":
                next_turn(input_until_equal("choose an option: trade,hunt ","trade","hunt"),settings,player_save,counter)
            else:
                next_turn(input_until_equal("choose an option: trade,farm","trade","plant"),settings,player_save,counter)
            counter+=1
        time["day"]+=1

game_loop(settings,player_save)