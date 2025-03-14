#print(board)
import random
def board_print(board):
    counter=0
    while counter < len(board):
        print(board[counter])
        counter=counter+1
def board_init(w,e):
    board = [[ 0 for col in range(w)] for row in range(e)]
    return(board)
def why_did_the_pawns_cross_the_board(w):
    board=board_init(3,3)
    board[2]=["k","1","1"]
    board_print(board)
def get_to_the_nine(w):
    board=board_init(5,5)
    board[2][2]=1
    board[4][4]=9
    x=2
    y=2
    while True:
        board[x][y]=1
        print(x)
        print(y)
        #print(counter)
        while counter < len(board):
            print(board[counter])
            counter=counter+1
        player_input=input("get to the nine! a,s,w or,d: ")
        if player_input=="w":
            if x==0:
                print("move invald")
            else:
                board[x][y]=0
                x=x-1
        elif player_input =="s":
            if x==4:
                print("move invald")
            else:
                board[x][y]=0
                x=x+1
        elif player_input =="d":
            if y==4:
               print("move invald")
            else:
                board[x][y]=0
                y=y+1  
        elif player_input=="a":
            if y==0:
                print("move invald")
            else:
                board[x][y]=0
                y=y-1     
        if x==4 and y==4:
            break
        board[x][y]=1  
    print("YOU WON!")
#get_to_the_nine(1)
why_did_the_pawns_cross_the_board(1)
