import urllib2
from Game import *

class Friend(object):  
    
     def __init__(self, name, url):
          self.name = name
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
          