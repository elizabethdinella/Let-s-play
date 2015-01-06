import urllib2
import random

from Game import *
from Friend import *
from User import *

while(True):    
    userUrl = raw_input("enter your steam profile URL ")
    numberOfFriends = raw_input("how many friends are you playing with? ")
    while not numberOfFriends.isdigit():
        numberOfFriends = raw_input("please enter a number ")
    
    numberOfFriends = int(numberOfFriends)    
        
    friendsList = []
    
    for i in range(0, numberOfFriends):
        friendsList.append(raw_input("enter your friend's screen name "))
    
    user = User(userUrl, numberOfFriends, friendsList)
    
    playersGames = [] 
    
    playersGames.append(user.games)
    for friend in user.friends:     
        playersGames.append(friend.games) 
        if len(friend.games) == 0:
            print friend.name, "has a private profile or no games!"
            print friend.name, "has been excluded from play."
            playersGames.remove(friend.games)
    
    for i in range(1, len(playersGames)):
        playersGames[0] &= (playersGames[i])
        
    commonGames = list(playersGames[0])
    
    if numberOfFriends > 0:
        if(len(commonGames) - 1 > 0):
            lastElement = commonGames[len(commonGames) - 1]
            loop = True  
            i = 0
            while(loop):
                if(commonGames[i] == lastElement):
                    loop = False
                if(not commonGames[i].isMultiplayer()):
                    if(commonGames[i] == lastElement):
                        commonGames.remove(commonGames[i])
                        break
                    commonGames.remove(commonGames[i])
                if(commonGames[i] != lastElement):    
                    i += 1
            
    reroll = True
    
    while(reroll and len(commonGames) > 0):
        randGame = random.randint(0, len(commonGames)-1)
        print "  __              __                       ___ \n /\ \            /\ \__                   /\_ \ \n \ \ \         __\ \ ,_\   ____      _____\//\ \      __     __  __ \n  \ \ \  __  /'__`\ \ \/  /',__\    /\ '__`\\\\ \ \   /'__`\  /\ \/\ \ \n   \ \ \L\ \/\  __/\ \ \_/\__, `\   \ \ \L\ \\\\_\ \_/\ \L\.\_\ \ \_\ \ \n    \ \____/\ \____\\\\ \__\/\____/    \ \ ,__//\____\ \__/.\_\\\\/`____ \ \n     \/___/  \/____/ \/__/\/___/      \ \ \/ \/____/\/__/\/_/ `/___/> \ \n                                       \ \_\                     /\___/ \n                                        \/_/                     \/__/ \n  %s!" %(commonGames[randGame].name)
        print
        reroll = raw_input("Reroll? (Y/N) ")
        while reroll == "l":
            for game in commonGames:
                print game
            reroll = raw_input("Reroll? (Y/N) ")
        reroll = (reroll.lower() == "y" or reroll == "")
        
    if(len(commonGames) == 0):
        print "No games in common :("
