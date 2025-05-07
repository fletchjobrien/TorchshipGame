# Gamestate tracking obj
from Map import Map
from Ship import Ship

class Gamestate:
 def __init__(self, map, playerfleet, aifleet, ai):
  if map == "Random":
   self.map = Map(playerfleet, aifleet)
  else:
   self.map = Map(playerfleet, aifleet)

  self.playerfleet = playerfleet
  self.aifleet = aifleet
  self.ai = ai

 def printMap(self):
  row = ""
  for i in self.map.map:
   if i.occupier != "Empty":
    if i.occupier.hp <= 0:
     i.occupier = "Empty"
    else:
     row += " S "

   elif i.terrain == "Asteroid":
    row += " A "
   elif i.terrain == "Planet":
    row+= " P "
   elif i.terrain == "Black Hole":
    row+= " B "
   else:
    row += " E "

   if len(row) >= 36:
    print(row)
    row = ""
