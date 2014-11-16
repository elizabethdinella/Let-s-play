import urllib2

def extract(source, criteria):
     criteria = '"' + criteria + '":'
     source = source[source.find(criteria) + len(criteria):]
     source = source[:source.find(',"')]
     return source
     
class Game(object):  
    
     def __init__(self, gameInfo):
          self.name = extract(gameInfo, "name")
          self.name = self.name[1:len(self.name) - 1]
          self.appid = extract(gameInfo, "appid")
          
     def isMultiplayer(self):
          page = urllib2.urlopen("http://store.steampowered.com/app/%s/" %(self.appid))
          source = page.read()
          return source.find('"Multiplayer"') != -1
     
     def __str__(self):
          return self.name
     
     def __eq__(self, other):
          return self.name == other.name  
     
     def __hash__(self):
          return hash(self.name)