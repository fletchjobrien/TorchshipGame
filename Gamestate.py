# Gamestate tracking obj
from Map import Map

gamemap = Map()

def printMap():
 row = ""
 for i in gamemap.map:
  if i.terrain == "Asteroid":
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

printMap()
