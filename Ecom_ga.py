import random
from reusable_functions import input_until_equal
from reusable_functions import input_until_equal_except_excluded
from reusable_functions import input_until_in_range

def gather_names(players):
    player_names=[]
    for x in range(players):
        while True:
            player_name=input("player "+str(x+1)+" whats your name?:")
            if input_until_equal("is this name correct?:"+player_name+" ",("yes","no"))=="yes":
                player_names.append(player_name)
                break
    return player_names

def gather_settings():
    #players=input_until_in_range("enter number of players(less than six):",(1,6))
    #player_names=gather_names(players)
    #turns_in_month=input_until_in_range("how many turns/days in each month:",(2,1000))
    turns_in_month=2
    players=2
    player_names=["Jeff","Connor"]
    #years=input_until_less_or_greater("how many years. 12 months in one year:",2,1)
    years=2
    return {"years":int(years),
            "turns in month":int(turns_in_month),
            "player amount":int(players),
            "player names":player_names}

def create_players(player_amount):
    resoures={"meat":{"deer":0},
              "vegetables":{"potato":0}}
    player_saves=[{"resoures":resoures},{"resoures":resoures},{"resoures":resoures},{"resoures":resoures},{"resoures":resoures}]
    counter=0
    while counter < player_amount:
        print("player"+str(counter+1))
        #pro=input_until_equal("choose your profession. farmer,hunter:","farmer","hunter")
        #pro="farmer"
        pro="hunter"
        player_saves[counter]["profession"]=pro
        player_saves[counter]["resoures"]=resoures
        if pro=="farmer":
            player_saves[counter]["resoures"]["vegetables"]["potato"]=10
        counter+=1
    return(player_saves)


def print_player_names(settings,current_player_num):
    print("you can trade with:")
    print("")
    for x in range(settings["player amount"]):
        if x!=current_player_num:
            print("player:"+settings["player names"][x])
    print("")

def print_player_resources(player_saves,current_player_num):
    print("your resources:")
    print("")
    print("meat:")
    for resource,amount in player_saves[current_player_num]["resoures"]["meat"].items():
        print(resource+":"+str(amount))
    print("")
    print("vegetables:")    
    for resource,amount in player_saves[current_player_num]["resoures"]["vegetables"].items():
        print(resource+":"+str(amount))
    print("")

def offer(player_resoures):
    input_until_in_range("how much do you want to trade?:",(1,1000))

def ask_interested_in_trade(player_saves,current_player_num,settings,wanted_resource):
    print("")
    print("")
    print("")
    #text=settings["player names"][x]+" do you want to trade your "+wanted_resource+" with "+settings["player names"][current_player_num]+"? (y/n)"
    players_interested={}
    for x in range(settings["player amount"]):
        if x!=current_player_num:
            if player_saves[x]["resoures"]["vegetables"][wanted_resource[0]]>0: #or player_saves[x]["resoures"]["meat"][wanted_resource[0]]>0:
                if input_until_equal(settings["player names"][x]+" do you want to trade your "+wanted_resource[0]+" with "+settings["player names"][current_player_num]+"? (y/n)",("y","n")).lower() =="y":
                    offer(player_saves[x]["resoures"])

def find_path(wanted_resource,resources):
    path=[]
    #resoures={"meat":{"deer":0},"vegetables":{"potato":0}}
    for category,items in resources.items():
        for item in items.keys():
            if item==wanted_resource[0]:
                path.append(category)
                path.append(item)
                return path
            
def ask_resource(player_saves,current_player_num,settings):
     print_player_resources(player_saves,current_player_num)
     wanted_resource=(input_until_equal("What resource would you trade for?:",("deer","potato")),input_until_in_range("Enter the amount you want:",(1,1000)))
     return wanted_resource

def trade(settings,current_player_num,player_saves):
    text={"1":"input the player you want to trade with or enter cancel: ",
          "2":"You can not trade with yourself"}
    if settings["player amount"]==1:
        print("there's no one around to trade with")
        return ""
    wanted_resource=ask_resource(player_saves,current_player_num,settings)
    path_to_wanted_resource=find_path(wanted_resource,player_saves[current_player_num]["resoures"])
    print(path_to_wanted_resource)
    ask_interested_in_trade(player_saves,current_player_num,settings,wanted_resource)
    enterable_values=settings["player names"].append("cancel")         
    print_player_names(settings,current_player_num)
    player_chosen=input_until_equal_except_excluded(text["1"],text["2"],enterable_values,settings["player names"][current_player_num])
    if player_chosen=="cancel":
        return ""


def add_events(player_save,player_amount):
        player_events=[]
        custom_events={"hunter":["hunt1","hunt2","hunt3"],"farmer":["farm1","farm2"]}
        for x in range(player_amount):
            standard_events=["trade"]
            standard_events.extend(custom_events[player_save[x]["profession"]])
            personalized_events=standard_events
            player_events.append(personalized_events)
        return player_events   

def add_events_to_text(text,events):
    for x in range(len(events)):
        text+=events[x]
        if x!=len(events)-1:
            text+=", "
    text+=":"        
    return text

def choose_event(settings,player_saves,current_player_num):
    current_player_save=player_saves[current_player_num]
    current_player_events=settings["events"][current_player_num]
    while True:
        choice=input_until_equal(add_events_to_text("choose an option: ",current_player_events),current_player_events)
        choice="trade"
        if choice=="trade":
               updated_player_save=trade(settings,current_player_num,player_saves)
        if updated_player_save!="":
            return updated_player_save
        

def clock(time,settings):
        months=["Mar","Apr","May","Jun","Jul","Aug","sep","Oct","Nov","Dec","Jan","Feb"]
        if time["day"]==settings["turns in month"]:
            time["day"]=0
            time["month"]+=1
        if time["month"]==len(months):
            time["month"]=0
            time["year"]+=1
        return time,months[time["month"]]


def game_loop(settings,player_saves):
    time={"year":1,
          "month":0,
          "day":0}
    while time["year"]<settings["years"]:
        counter=0
        time,current_month=clock(time,settings)
        while counter<settings["player amount"]:
            print(time)
            #print("year:"+str(time["year"]))
            #print("month:"+str(current_month))
            #print("day:"+str(time["day"]+1))
            print(settings["player names"][counter]+" it is your turn :)")
            choose_event(settings,player_saves,counter)
            counter+=1
        time["day"]+=1


settings=gather_settings()
player_saves=create_players(settings["player amount"])
settings["events"]=add_events(player_saves,settings["player amount"])
game_loop(settings,player_saves)