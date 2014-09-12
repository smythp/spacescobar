## Ask for number of players and return #

def askplayer():
    while True:
        try:
            playernum = int(input("Number of players?"))
            if checkvalid(playernum) == 0:
                print("Enter a number between 1 and 4.")
            elif playernum == 1:
                print("%s player" % playernum)
                return(playernum)
            else:
                print("%s players" % playernum)
                return(playernum)
        except ValueError:
            print("Enter a number between 1 and 4.")

## Check if what the player enters is 1, 2, 3, or 4

def checkvalid(x):
    valid_4 = [1,2,3,4]
    return(valid_4.count(x))

## Choose a faction

def choosefaction(pnumber):
    fac_list = []
    num_write = {1:'one',2:'two',3:'three',4:'four'}
    for x in range(0,pnumber):
        while 1:
            try:
                f = int(input("What faction is player %s?" % num_write[x+1]))
                if checkvalid(f) == 0:
                    print("Enter a number between 1 and 4.")
                else:
                    fac_list.append(f)
                    break
            except ValueError:
                print("Enter a number between 1 and 4.")
    return(fac_list)


playernum = askplayer()
factions = choosefaction(playernum)
num_write = {1:'one',2:'two',3:'three',4:'four'}
fac_dict = {1:'Bankers',2:'DarkNet',3:'Bold Alpha Eagle Alpha',4:'Oligarchs'}
f_one = factions[0]
f_two = factions[1]
f_three = factions[2]
f_four = factions[3]

# Tell who is playing what
print('')
for x in range(0,playernum):
    print("Player %s is playing as %s" % (num_write[x + 1],fac_dict[factions[x]]))





    
