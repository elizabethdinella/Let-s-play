import urllib2
from Game import *
from Friend import *

class User(object):  
    
     def __init__(self, url, numberOfFriends, listOfFriends):
          self.games = set()
          page = urllib2.urlopen(url + "/games/?tab=all")
          source = page.read()

          source = source[source.find("var rgGames = [{"):]
          source = source[:source.find("\n"):]

          argument = source[source.find('[{'):]
          argument = argument[:argument.find('},{')]
          self.games.add(Game(argument))
          source = source[len(argument):]
          
          while(source.find(',{') != -1):
               argument = source[source.find(',{'):]
               if(argument.find('},{') != -1):
                    argument = argument[:argument.find('},{')]
               elif(argument.find('}]') != -1):    
                    argument = argument[:argument.find('}]')]
               self.games.add(Game(argument))
               source = source[len(argument):]              
          
          self.friends = []
               
          page = urllib2.urlopen(url + "/friends/")
          source = page.read()
               
          for i in range(0, numberOfFriends):
               temp = source[:source.find(listOfFriends[i])]
               urlTag = '<a class="friendBlockLinkOverlay" href="'
               temp = temp[temp.rfind(urlTag)+len(urlTag):]
               temp = temp[:temp.find('"></a>')]
               self.friends.append(Friend(listOfFriends[i], temp))          